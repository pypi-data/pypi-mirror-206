import json
from common.common.constant import Constant
from common.data.handle_common import get_system_key
from common.common.api_driver import APIDriver
from loguru import logger


class ServicePlatForm(object):

    @classmethod
    def sendMsg(self, _data):
        try:
            _data = _data.encode()
            APIDriver.http_request(url=get_system_key(Constant.MSG_URL), method='post', parametric_key='data',
                                       data=_data)
            logger.info(f'推送人:{_arr[0]} 邮箱:{_arr[1]} 推送成功')
        except Exception as e:
            logger.info(f'推送人:{_arr[0]} 邮箱:{_arr[1]}  异常信息' + repr(e))

    @classmethod
    def getCaseByCycle(self, cycleId, caseName, status, caseId: str = '00000'):
        try:
            response = APIDriver.http_request(url=Constant.ATF_PYTHON_URL+'/jira/cycle/getCase',
                                   method = 'post',
                                   parametric_key = 'json',
                                   data = {"cycleId":cycleId,"caseName":caseName,"caseId":caseId,"status":status},
                                    )
            content = json.loads(response.content)
            return content
        except Exception as e:
            logger.error(f'获取周期编号：{cycleId} 用例名称:{caseName} 状态:{status}  用例编号:{caseId}  异常信息' + repr(e))

    @classmethod
    def getATFData(self, projectAlice, env):
        try:
            response = APIDriver.http_request(url=Constant.ATF_API + f'/getParam/{projectAlice}/{env}',
                                              method='get',
                                              )
            content = json.loads(response.content)['data']
            logger.info(f'获取数据项目别名：{projectAlice} 环境:{env}  配置信息' + json.dumps(content, ensure_ascii=False))
            return content
        except Exception as e:
            logger.error(f'获取数据项目别名：{projectAlice} 环境:{env}  异常信息' + repr(e))







