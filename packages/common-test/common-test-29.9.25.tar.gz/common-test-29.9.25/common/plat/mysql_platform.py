import datetime
from loguru import logger
from common.db.handle_db import MysqlDB
from common.data.handle_common import get_system_key,format_caseName
from common.common.constant import Constant
from common.plat.jira_platform import JiraPlatForm
from common.data.data_process import DataProcess


class MysqlPlatForm(object):

    @classmethod
    def sync_mysql_data(self, _caselist):
        logger.info("开始同步Jira测试计划周期用例信息到数据库")
        _dataList = []
        jirakey = get_system_key(Constant.ISSUE_KEY)
        cycleId = get_system_key(Constant.TEST_SRTCYCLE_ID)
        cycleName = get_system_key(Constant.TEST_SRTCYCLE_NAME)
        _date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        _config = {'key':'traffic','env':'test'}
        _mysql = MysqlDB(_config)
        for _caseInfo in _caselist:
            _caseKey = _caseInfo['testCaseKey']
            _caseName = format_caseName(_caseInfo['summary'])
            _temp = (jirakey, cycleId, cycleName,
                     _caseName, _caseInfo['id'], _caseInfo['testCaseKey'],
                     _caseInfo['status'], _date)
            _dataList.append(_temp)
            _sql = f"select * from `traffic_test`.`test_autotest_meta` where caseid='{_caseKey}'"
            _info = _mysql.execute(_sql).fetchall()
            if len(_info) == 0:
                jira_key, case_name, case_link, case_priority, case_model, case_suit, case_story_id, case_story_name, case_story_link, cast_type = \
                    JiraPlatForm.getCaseInfo(_caseKey)
                case_name = format_caseName(_caseInfo['summary'])
                caseid = _caseInfo['testCaseKey']
                _sql = f"INSERT INTO `traffic_test`.`test_autotest_meta`(`casename`, `caseid`, `caselink`, `casepriority`, `casemodel`, `casesuit`, `casestoryid`, `casestoryname`, `casestorylink`, `casetype`, `create_time`) " \
                       f"VALUES ('{case_name}',  '{caseid}', '{case_link}','{case_priority}','{case_model}','{case_suit}','{case_story_id}','{case_story_name}','{case_story_link}','{cast_type}','{_date}')"
                _mysql.execute(_sql)
            _sqlscript = f"select * from `traffic_test`.`test_autotest_script` where testname='{_caseName}'"
            _infoscript = _mysql.execute(_sql).fetchall()
            if len(_infoscript) == 0:
                scriptUrl=JiraPlatForm.getTestReference(_caseKey)
                if DataProcess.isNotNull(scriptUrl):
                    MysqlPlatForm.insert_test_autotest_script(_caseName, _caseKey, scriptUrl)
        _sql = f"delete from `traffic_test`.`test_autotest_run` where jirakey='{jirakey}' and cycleId='{cycleId}'"
        _mysql.execute(_sql)
        _sqlbatch = f"INSERT INTO `traffic_test`.`test_autotest_run`(`jirakey`, `cycleId`, `cyclename`, `casename`, `caserunid`, `caseid`, `status`, `create_time`) " \
                    f"VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        _mysql.executemany(_sqlbatch, _dataList)
        _mysql.close()
        logger.info("同步Jira测试计划周期用例信息到数据库完成")

    @classmethod
    def insert_test_autotest_script(self, testname, caseid, caseurl):
        if DataProcess.isNotNull(get_system_key(Constant.GIT_PROJECTNAME)):
            testname,gitname,scripturl, scriptclass, scriptmethod, scriptname = DataProcess.getCaseUrlMeta(testname, caseurl)
            if DataProcess.isNotNull(scripturl):
                JiraPlatForm.updateDescription(caseid, scripturl)
                JiraPlatForm.updateTestReference(caseid, caseurl)
                _config = {'key': 'traffic', 'env': 'test'}
                _mysql = MysqlDB(_config)
                sql = f"select distinct(caseurl) from test_autotest_script where `status` = '0' and gitname ='{gitname}' and testname='{testname}' and caseurl='{caseurl}'"
                _list = _mysql.execute(sql).fetchall()
                if _list is None or _list.__len__() < 1:
                    _date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    _sql = f"INSERT INTO `traffic_test`.`test_autotest_script`(`gitname`, `suitname`, `tagversion`, `testid`, `testname`, `scriptclass`, `scriptmethod`, `scriptname`, `scriptpackage`, `status`, `updatetime`, `caseurl`, `scripturl`) " \
                           f"VALUES ('{gitname}', '', 'run', '{caseid}', '{testname}', '{scriptclass}', '{scriptmethod}', '{scriptname}', '', '0', '{_date}', '{caseurl}', '{scripturl}')"
                    _mysql.execute(_sql)
                    logger.info(f'保存用例和脚本关系成功：用例名称:{testname} 脚本路径:{caseurl}')
                _mysql.conn.commit()
                _mysql.close()

    @classmethod
    def sync_autotest_script(self, testname, caseid, caseurl):
        if DataProcess.isNotNull(get_system_key(Constant.GIT_PROJECTNAME)):
            testname, gitname, scripturl, scriptclass, scriptmethod, scriptname = DataProcess.getCaseUrlMeta(testname,
                                                                                                             caseurl)
            if DataProcess.isNotNull(scripturl):
                if caseid != '00000':
                    JiraPlatForm.updateDescription(caseid, scripturl)
                    JiraPlatForm.updateTestReference(caseid, caseurl)
                _config = {'key': 'traffic', 'env': 'test'}
                _mysql = MysqlDB(_config)
                sql = f"delete from test_autotest_script where testname='{testname}' and gitname='{gitname}'"
                _list = _mysql.execute(sql)
                _mysql.conn.commit()
                _date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                _sql = f"INSERT INTO `traffic_test`.`test_autotest_script`(`gitname`, `suitname`, `tagversion`, `testid`, `testname`, `scriptclass`, `scriptmethod`, `scriptname`, `scriptpackage`, `status`, `updatetime`, `caseurl`, `scripturl`) " \
                       f"VALUES ('{gitname}', '', 'run', '{caseid}', '{testname}', '{scriptclass}', '{scriptmethod}', '{scriptname}', '', '0', '{_date}', '{caseurl}', '{scripturl}')"
                _mysql.execute(_sql)
                _mysql.conn.commit()
                _mysql.close()
                logger.info(f'保存用例和脚本关系成功：用例名称:{testname} 脚本路径:{caseurl}')

    @classmethod
    def insert_api_data(self, _url, _methond, _header, _data, _reponse_time,_reponse_code):
        _hash = hash(f'{_url}:{_methond}:{_header}:{_data}:{_reponse_time}')
        _data= str(_data).replace("'","")
        _config = {'key':'traffic','env':'test'}
        _date=datetime.datetime.now()
        _sql=f"INSERT INTO `traffic_test`.`base_api_data`(`hash_id`, `url`,`method`, `data`, `reponse_time`,`reponse_code`, `create_time`) VALUES ('{_hash}', '{_url}', '{_methond}', '{_data}', '{_reponse_time}', '{_reponse_code}','{_date}')"
        _mysql = MysqlDB(_config)
        _mysql.execute(_sql)
        _mysql.conn.commit()
        _mysql.close()

    @classmethod
    def getScriptyPathByCaseNameList(self, CaseNameList):
        _config = {'key':'traffic','env':'test'}
        _mysql = MysqlDB(_config)
        sql = f"select distinct(caseurl) from test_autotest_script where `status` = '0'"
        sql += " and testname in (%s)" % ','.join(["'%s'" % testname for testname in CaseNameList])
        _list = _mysql.execute(sql).fetchall()
        _mysql.close()
        return _list


    @classmethod
    def insert_test_autotest_batchrun(self, data):
        _config = {'key':'traffic','env':'test'}
        _sqlbatch = f"INSERT INTO `traffic_test`.`test_autotest_run`(`jirakey`, `cycleId`, `cyclename`, `casename`, `caserunid`, `caseid`, `status`, `create_time`) " \
               f"VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        _mysql = MysqlDB(_config)
        _mysql.executemany(_sqlbatch, data)
        _mysql.close()

    @classmethod
    def insert_test_autotest_meta(self, casename, caseid, case_link,case_priority, case_model, case_suit, case_story_id, case_story_name, case_story_link):
        _config = {'key':'traffic','env':'test'}
        _date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        _sql = f"INSERT INTO `traffic_test`.`test_autotest_meta`(`casename`, `caseid`, `caselink`, `casepriority`, `casemodel`, `casesuit`, `casestoryid`, `casestoryname`, `casestorylink`, `create_time`) " \
               f"VALUES ('{casename}',  '{caseid}', '{case_link}','{case_priority}','{case_model}','{case_suit}','{case_story_id}','{case_story_name}','{case_story_link}','{_date}')"
        _mysql = MysqlDB(_config)
        _mysql.execute(_sql)
        _mysql.conn.commit()
        _mysql.close()


    @classmethod
    def get_case_meta_ByID(self, caseID):
        _config = {'key':'traffic','env':'test'}
        _sql = f"select * from `traffic_test`.`test_autotest_meta` where caseid='{caseID}'"
        _mysql = MysqlDB(_config)
        _info = _mysql.execute(_sql).fetchall()
        return _info

    @classmethod
    def get_case_meta_ByName(self, casename):
        _config = {'key':'traffic','env':'test'}
        _sql = f"select * from `traffic_test`.`test_autotest_meta` where casename='{casename}'"
        _mysql = MysqlDB(_config)
        _info = _mysql.execute(_sql).fetchall()
        return _info

    @classmethod
    def delete_test_autotest_run(self, jirakey, cycleId):
        _config = {'key':'traffic','env':'test'}
        _sql = f"delete from `traffic_test`.`test_autotest_run` where jirakey='{jirakey}' and cycleId='{cycleId}'"
        _mysql = MysqlDB(_config)
        _mysql.execute(_sql)
        _mysql.close()

    @classmethod
    def get_test_autotest_run(self, jirakey, cycleId, result:str="'通过','未执行','失败','自动化执行'"):
        _info = []
        _sql = f"select * from `traffic_test`.`test_autotest_run` where jirakey='{jirakey}' and cycleId='{cycleId}' and status in ({result})"
        try:
            _config = {'key':'traffic','env':'test'}
            _mysql = MysqlDB(_config)
            _info = _mysql.execute(_sql).fetchall()
            return _info
        except Exception as e:
            logger.info(f'查询SQL异常：{_sql}')
            return _info

    @classmethod
    def get_test_case_info(self, jirakey, cycleId, caseName):
        _config = {'key':'traffic','env':'test'}
        _sql = f"select * from `traffic_test`.`test_autotest_run` where jirakey='{jirakey}' and cycleId='{cycleId}' and casename='{caseName}'"
        _mysql = MysqlDB(_config)
        _info = _mysql.execute(_sql).fetchall()
        return _info

    @classmethod
    def get_test_case_info_ByID(self, jirakey, cycleId, caseid):
        _config = {'key':'traffic','env':'test'}
        _sql = f"select * from `traffic_test`.`test_autotest_run` where jirakey='{jirakey}' and cycleId='{cycleId}' and caseid='{caseid}'"
        _mysql = MysqlDB(_config)
        _info = _mysql.execute(_sql).fetchall()
        return _info

    @classmethod
    def update_test_case_info_ByRunID(self, jirakey, cycleId, caserunid, status):
        _config = {'key':'traffic','env':'test'}
        if status == 'passed':
            status = '通过'
        if status == 'failed':
            status = '失败'
        if status == 'broken':
            status = '中断'
        _date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        _sql = f"update `traffic_test`.`test_autotest_run` SET `status` = '{status}', `create_time` = '{_date}' where jirakey='{jirakey}' and cycleId='{cycleId}' and caserunid='{caserunid}'"
        _mysql = MysqlDB(_config)
        _info = _mysql.execute(_sql).fetchall()
        return _info

    @classmethod
    def update_autoTest_run(self, cycleId, status):
        _config = {'key': 'traffic', 'env': 'test'}
        if status == 'passed':
            status = '通过'
        if status == 'failed':
            status = '失败'
        if status == 'broken':
            status = '中断'
        _date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logger.info(f'更新数据库测试周期:{cycleId} 状态:{status}')
        _sql = f"update `traffic_test`.`test_autotest_run` SET `status` = '{status}', `create_time` = '{_date}' where cycleId='{cycleId}'"
        _mysql = MysqlDB(_config)
        _info = _mysql.execute(_sql).fetchall()
        _mysql.conn.commit()
        _mysql.close()
        return _info

    @classmethod
    def get_api_data(self, _url, _methond, _header, _data, _reponse_time, _reponse_code):
        _config = {'key':'traffic','env':'test'}
        _sql = f"select * from `traffic_test`.`base_api_data` where `url`='{_url}' and `method`='{_methond}' and `data`='{_data}' and `reponse_code`={_reponse_code} "
        _mysql = MysqlDB(_config)
        _time=''
        _info=''
        for _temp in  _mysql.execute(_sql).fetchall():
            _time=str(_temp['reponse_time'])+"S, "+_time
            _info =str(_temp['create_time']) +"执行时间:"+str(_temp['reponse_time']) + "S, " + _info
        return _time,_info

    @classmethod
    def get_case_info(self, caseName):
        _config = {'key':'traffic','env':'test'}
        _sql = f"select * from test_autotest_script where testname = '{caseName}'"
        _caseInfo = []
        try:
            _mysql = MysqlDB(_config)
            _caseInfo = _mysql.execute(_sql).fetchall()
            return _caseInfo
        except Exception as e:
            logger.info(f'执行sql语句异常{_sql}')
            return _caseInfo



