import asyncio
import datetime
from enum import IntEnum
import hashlib
import json
import httpx
from random import randint

from growattRequestsAsync.exceptions import LoginFailedException, FetchFailedException, InvalidTimespanException


class Timespan(IntEnum):
    HOUR = 0
    DAY = 1
    MONTH = 2


def hash_password(password: str) -> str:
    """
    Generate MD5 hash for password
    :param password: password
    :return: MD5 hash
    """
    password_md5 = hashlib.md5(password.encode('utf-8')).hexdigest()
    for i in range(0, len(password_md5), 2):
        if password_md5[i] == '0':
            password_md5 = password_md5[0:i] + 'c' + password_md5[i + 1:]
    return password_md5


def date_to_str(timespan=None, date=None):
    """
    convert datetime object to str
    :param timespan: Timespan in days (1) or months (2)
    :param date: datetime object to convert to str
    :raises:
        InvalidTimespanException: Invalid timespan value
    :return: string representation of date
    """
    if timespan is not None and timespan not in Timespan:
        raise InvalidTimespanException()

    if date is None:
        date = datetime.datetime.now()

    if timespan == Timespan.MONTH:
        date_str = date.strftime('%Y-%m')
    else:
        date_str = date.strftime('%Y-%m-%d')

    return date_str


class GrowattRequests:
    SERVER_URL = "https://server.growatt.com/"
    DEFAULT_USER_AGENT = "Mozilla/5.0 (Linux; Android 13; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) " \
                         "Chrome/112.0.5615.135 Mobile Safari/537.36 "

    def __init__(self, user_agent_randomness: bool = False, user_agent: str = None) -> None:
        """
        Constructor to initialize GrowattAPI object
        :param user_agent_randomness: add randomness to user-agent
        :param user_agent: user agent string
        """
        if user_agent is not None:
            self.user_agent = user_agent
        else:
            self.user_agent = self.DEFAULT_USER_AGENT

        if user_agent_randomness:
            # add randomness to user agent
            randomness = ''.join(["{}".format(randint(0, 9)) for num in range(0, 9)])
            self.user_agent += " - " + randomness

        self.client = httpx.AsyncClient()

        headers = {'User-Agent': self.user_agent}
        self.client.headers.update(headers)

    def get_url(self, suffix: str) -> str:
        """
        Function to create the full API endpoint URL
        :param suffix: API endpoint (suffix)
        :return: full URL (server_url+suffix)
        """
        return f"{self.SERVER_URL}{suffix}"

    async def login(self, username: str, password: str, is_password_hashed: bool = False) -> dict:
        """
        User login.
        :param username: username
        :param password: password
        :param is_password_hashed: password is hashed flag (MD5)
        :raises:
            LoginFailedException: login failed
            FetchFailedException: received invalid response
        :return: 
            dict(
                "msg": str,
                "totalData": obj,
                "data": [
                {
                    "plantId": str,
                    "plantName": str
                }
                ],
                "deviceCount": str,
                "isOpenDeviceList": int,
                "quality": str,
                "isCheckUserAuth": bool,
                "isEicUserAddSmartDevice": bool,
                "isOpenDeviceParams": int,
                "isViewDeviceInfo": bool,
                "success": bool,
                "service": str,
                "user": {
                    "agentCode": str,
                    "phoneNum": str,
                    "cpowerToken": str,
                    "type": int,
                    "vipPoints": int,
                    "approved": bool,
                    "password": str,
                    "rightlevel": int,
                    "isAgent": int,
                    "userIconPath": str,
                    "serverUrl": str,
                    "inverterList": list,
                    "id": int,
                    "lat": str,
                    "area": str,
                    "lng": str,
                    "kind": int,
                    "nickName": str,
                    "parentUserId": int,
                    "timeZone": int,
                    "accountName": str,
                    "counrty": str,
                    "inverterGroup": list,
                    "customerCode": str,
                    "registerType": str,
                    "enabled": bool,
                    "lastLoginIp": str,
                    "userLanguage": str,
                    "isBigCustomer": int,
                    "uid": str,
                    "userDeviceType": int,
                    "installerEnable": str,
                    "appType": str,
                    "company": str,
                    "isValiPhone": int,
                    "appAlias": str,
                    "email": str,
                    "createDate": str,
                    "activeName": str,
                    "roleId": int,
                    "smsNotice": bool,
                    "wxOpenid": str,
                    "noticeType": str,
                    "isPhoneNumReg": int,
                    "isValiEmail": int,
                    "token": str,
                    "lastLoginTime": str,
                    "mailNotice": bool,
                    "accountNameOss": bool,
                    "dataAcqList": list,
                    "distributorEnable": str,
                    "codeIndex": int
                },
                "isOpenSmartFamily": int,
                "app_code": str,
                "userId": int,
                "userLevel": int
            )
        """
        if not is_password_hashed:
            password = hash_password(password)

        response = await self.client.post(self.get_url('newTwoLoginAPI.do'), data={
            "userName": username,
            "password": password
        })

        try:
            data = json.loads(response.content.decode("utf-8"))["back"]
            if data is None or not data.get("success", True):
                raise LoginFailedException()
        except json.decoder.JSONDecodeError as e:
            raise FetchFailedException()

        return data

    async def get_plant_list(self, user_id: int) -> dict:
        """
        Get a list of plants for this user
        :param user_id: user ID
        :raises:
            FetchFailedException: received invalid response
        :return:
            dict(
                "totalData": {
                    "CO2Sum": str,
                    "storagePDisCharge": str,
                    "storagePacToUser": str,
                    "currentPowerSum": str,
                    "isHaveStorage": str,
                    "todayEnergySum": str,
                    "eTotalMoneyText": str,
                    "totalEnergySum": str,
                    "storagePCharge": str,
                    "storageCapacity": str
                },
                "data": [
                    {
                        "storagePDisCharge": str,
                        "isHaveStorage": str,
                        "currentPower": str,
                        "totalEnergy": str,
                        "plantMoneyText": str,
                        "storagePCharge": str,
                        "plantId": str,
                        "storageCapacity": str,
                        "storageStatus": str,
                        "todayEnergy": str,
                        "plantName": str
                    }
                ],
                "success": bool
            }
        """
        response = await self.client.get(self.get_url("PlantListAPI.do"),
                                         params={"userId": user_id})
        try:
            data = json.loads(response.content.decode("utf-8"))["back"]
            if data is None or not data.get("success", True):
                raise FetchFailedException()
        except json.decoder.JSONDecodeError as e:
            raise FetchFailedException()

        return data

    async def get_plant_details(self, plant_id: str, timespan: Timespan, date: datetime.date = None) -> dict:
        """
        Get plant details for a given timespan (in days or months).
        :param plant_id: plant ID
        :param timespan: Timespan (DAY or MONTH)
        :param date: start date
        :raises:
            FetchFailedException: received invalid response
        :return:
            dict(
                "plantData": {
                    "plantMoneyText": str,
                    "plantId": str,
                    "currentEnergy": str,
                    "plantName": str
                },
                "data": {
                    "01": str,
                    "02": str,
                    "03": str,
                    ...
                    "31": str
                },
                "success": bool
            )
        """
        date_str = date_to_str(timespan, date)

        response = await self.client.get(self.get_url("PlantDetailAPI.do"), params={
            "plantId": plant_id,
            "type": timespan.value,
            "date": date_str
        })
        try:
            data = json.loads(response.content.decode("utf-8"))["back"]
            if data is None or not data.get("success", True):
                raise FetchFailedException()
        except json.decoder.JSONDecodeError as e:
            raise FetchFailedException()

        return data

    async def get_plant_info(self, plant_id: str) -> dict:
        """
        Get plant information and device list.
        :param plant_id: plant ID
        :return:
            dict(
                "isHaveOptimizer": int,
                "totalEnergy": str,
                "nominal_Power": int,
                "totalMoneyText": str,
                "optimizerType": int,
                "storageTodayPpv": str,
                "storagePuser": str,
                "Co2Reduction": str,
                "useEnergy": str,
                "nominalPower": int,
                "isHavePumper": str,
                "ammeterType": str,
                "invTodayPpv": str,
                "plantMoneyText": str,
                "deviceList": [
                    {
                        "deviceType": str,
                        "eChargeToday": str,
                        "apparentPower": str,
                        "deviceSn": str,
                        "deviceStatus": str,
                        "capacity": str,
                        "pCharge": str,
                        "lost": bool,
                        "datalogSn": str,
                        "storageType": str,
                        "location": str,
                        "deviceAilas": str,
                        "activePower": str,
                        "energy": str
                    }
                ],
                "todayEnergy": str,
                "todayDischarge": str,
                "storagePgrid": str
            )
        """
        response = await self.client.get(self.get_url("newTwoPlantAPI.do"), params={
            'op': "getAllDeviceList",
            "plantId": plant_id,
            "pageNum": 1,
            "pageSize": 1
        })

        try:
            data = json.loads(response.content.decode("utf-8"))
            if data is None or not data.get("success", True):
                raise FetchFailedException()
        except json.decoder.JSONDecodeError as e:
            raise FetchFailedException()

        return data

    async def get_plant_settings(self, plant_id: str) -> dict:
        """
        Get plant settings
        :param plant_id: plant ID
        :raises:
            FetchFailedException: received invalid response
        :return:
            dict(
                "formulaCo2": float,
                "companyName": str,
                "etodayCo2Text": str,
                "userBean": ???,
                "formulaSo2": float,
                "children": list,
                "plantFromBean": None,
                "id": int,
                "EYearMoneyText": str,
                "etotalCoalText": str,
                "etotalSo2Text": str,
                "plant_lng": str,
                "locationImgName": str,
                "deviceCount": int,
                "map_countryId": int,
                "mapLat": str,
                "prMonth": str,
                "etotalMoney": int,
                "plantType": int,
                "windAngle": int,
                "formulaMoney": int,
                "mapCity": str,
                "nominalPower": int,
                "logoImgName": str,
                "latitudeText": str,
                "userAccount": str,
                "storage_TodayToUser": int,
                "eventMessBeanList": list,
                "map_cityId": int,
                "createDateTextA": str,
                "status": int,
                "formulaMoneyUnitId": str,
                "energyMonth": int,
                "city": str,
                "prToday": str,
                "etodayCoalText": str,
                "currentPac": int,
                "parentID": str,
                "plantAddress": str,
                "envTemp": int,
                "formulaCoal": float,
                "treeID": str,
                "hasStorage": int,
                "storage_TotalToUser": int,
                "fixedPowerPrice": float,
                "etodaySo2Text": str,
                "panelTemp": int,
                "createDate": {
                    "date": int,
                    "hours": int,
                    "seconds": int,
                    "month": int,
                    "timezoneOffset": int,
                    "year": int,
                    "minutes": int,
                    "time": int,
                    "day": int
                },
                "map_provinceId": int,
                "pairViewUserAccount": str,
                "emonthSo2Text": str,
                "peakPeriodPrice": float,
                "hasDeviceOnLine": int,
                "storage_BattoryPercentage": int,
                "etodayMoney": int,
                "formulaTree": int,
                "moneyUnitText": str,
                "longitude_d": str,
                "country": str,
                "longitude_f": str,
                "etodayMoneyText": str,
                "longitude_m": str,
                "phoneNum": str,
                "storage_TodayToGrid": int,
                "designCompany": str,
                "currentPacStr": str,
                "etotalMoneyText": str,
                "windSpeed": int,
                "valleyPeriodPrice": int,
                "latitude_f": str,
                "mapLng": str,
                "latitude_d": str,
                "level": int,
                "latitude_m": str,
                "energyYear": int,
                "longitudeText": str,
                "flatPeriodPrice": float,
                "emonthCoalText": str,
                "paramBean": None,
                "etotalCo2Text": str,
                "imgPath": str,
                "isShare": bool,
                "plant_lat": str,
                "emonthCo2Text": str,
                "timezone": int,
                "storage_eChargeToday": int,
                "remark": int,
                "storage_TotalToGrid": int,
                "defaultPlant": bool,
                "createDateText": str,
                "currentPacTxt": str,
                "unitMap": {
                    "CHF": "CHF",
                    "NT": "nt",
                    "ZAR": "zar",
                    "INR": "inr",
                    "VND": "vnd",
                    "AUD": "aud",
                    "ILS": "ils",
                    "JPY": "jpy",
                    "PLN": "pln",
                    "GBP": "gbp",
                    "KHR": "khr",
                    "IDR": "idr",
                    "HUF": "huf",
                    "PHP": "php",
                    "BUK": "buk",
                    "TRY": "try",
                    "THP": "thp",
                    "ISK": "isk",
                    "HKD": "hkd",
                    "EUR": "eur",
                    "DKK": "dkk",
                    "RMB": "rmb",
                    "CAD": "cad",
                    "MYR": "myr",
                    "USD": "usd",
                    "NOK": "nok",
                    "Euro": "euro",
                    "SGD": "sgd",
                    "LKR": "lkr",
                    "BRC": "brc",
                    "CZK": "czk",
                    "PKR": "pkr",
                    "LAK": "lak",
                    "REAL": "REAL",
                    "SEK": "sek",
                    "NZD": "nzd",
                    "DOLLAR": "dollar",
                    "UAH": "uah",
                    "ARP": "arp"
                },
                "alarmValue": int,
                "treeName": str,
                "alias": str,
                "irradiance": int,
                "formulaMoneyStr": str,
                "onLineEnvCount": int,
                "storage_eDisChargeToday": int,
                "timezoneText": str,
                "dataLogList": list,
                "map_areaId": int,
                "etotalFormulaTreeText": str,
                "plantImgName": str,
                "eToday": int,
                "eTotal": int,
                "emonthMoneyText": str,
                "nominalPowerStr": str,
                "plantName": str
            )
        """
        response = await self.client.get(self.get_url("newPlantAPI.do"), params={
            "op": "getPlant",
            "plantId": plant_id
        })
        try:
            data = json.loads(response.content.decode("utf-8"))
            if data is None or not data.get("success", True):
                raise FetchFailedException()
        except json.decoder.JSONDecodeError as e:
            raise FetchFailedException()

        return data

    async def get_device_list(self, plant_id: str) -> dict:
        """
        Get list of all devices in a given plant
        :param plant_id: plant ID
        :raises:
            FetchFailedException: received invalid response
        :return:
            dict(
                [
                    dict(
                        "deviceType": str,
                        "eChargeToday": str,
                        "apparentPower": str,
                        "deviceSn": str,
                        "deviceStatus": str,
                        "capacity": str,
                        "pCharge": str,
                        "lost": bool,
                        "datalogSn": str,
                        "storageType": str,
                        "location": str,
                        "deviceAilas": str,
                        "activePower": str,
                        "energy": str
                    )
                ]
            )
        """
        return (await self.get_plant_info(plant_id))["deviceList"]

    async def get_storage_energy_overview(self, plant_id: str, storage_device_sn: str) -> dict:
        """
        Get high-level energy generation/usage data.
        :param plant_id: plant ID
        :param storage_device_sn: storage device serial number: deviceSn in deviceList
        :raises:
            FetchFailedException: received invalid response
        :return:
            dict(
                "eChargeTotal": str,
                "eChargeToday": str,
                "eToUserTotal": str,
                "useEnergyToday": str,
                "epvToday": str,
                "eDischargeTotal": str,
                "epvTotal": str,
                "eDischargeToday": str,
                "eToGridToday": str,
                "eToUserToday": str,
                "useEnergyTotal": str,
                "eToGridTotal": str
            )
        """
        response = await self.client.post(self.get_url("newStorageAPI.do?op=getEnergyOverviewData_sacolar"), params={
            "plantId": plant_id,
            "storageSn": storage_device_sn
        })
        try:
            data = json.loads(response.content.decode("utf-8"))["obj"]
        except json.decoder.JSONDecodeError as e:
            raise FetchFailedException()

        return data

    async def get_storage_params(self, storage_device_sn: str) -> dict:
        """
        Get storage device parameters.
        :param storage_device_sn: storage device serial number
        :raises:
            FetchFailedException: received invalid response
        :return: massive dict containing all storage device parameters
        """
        response = await self.client.get(self.get_url("newStorageAPI.do"), params={
            "op": "getStorageParams_sacolar",
            "storageId": storage_device_sn
        })
        try:
            data = json.loads(response.content.decode("utf-8"))
            if data is None or not data.get("success", True):
                raise FetchFailedException()
        except json.decoder.JSONDecodeError as e:
            raise FetchFailedException()

        return data

    async def get_storage_details(self, storage_device_sn: str) -> dict:
        """
        Get storage device details.
        :param storage_device_sn: storage device serial number
        :raises:
            FetchFailedException: failed to fetch data from the endpoint
        :return:
            dict(
                "vpv2": str,
                "eBatDisChargeTotal": str,
                "batSn": str,
                "vpv1": str,
                "pCharge1": str,
                "outPutPower": str,
                "pCharge2": str,
                "loadPercent": str,
                "apparentPower": str,
                "vbat": str,
                "eBatChargeToday": str,
                "iChargePV1": str,
                "freqGrid": str,
                "iChargePV2": str,
                "outPutVolt": str,
                "capacity": str,
                "freqOutPut": str,
                "epvToday": str,
                "eBatChargeTotal": str,
                "epvTotal": str,
                "vGrid": str,
                "eBatDisChargeToday": str,
                "activePower": str
            )
        """
        response = await self.client.get(self.get_url("newStorageAPI.do"), params={
            "op": "getStorageInfo_sacolar",
            "storageId": storage_device_sn
        })
        try:
            data = json.loads(response.content.decode("utf-8"))
            if data is None or not data.get("success", True):
                raise FetchFailedException()
        except json.decoder.JSONDecodeError as e:
            raise FetchFailedException()

        return data

    async def get_inverter_data(self, inverter_sn: str, date: datetime.date = None) -> dict:
        """
        Get PV inverter data for a given date
        :param inverter_sn: PV inverter serial number (can be found in deviceList)
        :param date: datetime.date object (defaults to now)
        :raises:
            FetchFailedException: failed to fetch data from endpoint
        :return: dict
        """
        date_str = date_to_str(date=date)
        response = await self.client.get(self.get_url("newInverterAPI.do"), params={
            "op": "getInverterData",
            "id": inverter_sn,
            "type": 1,
            "date": date_str
        })
        try:
            data = json.loads(response.content.decode("utf-8"))
            if data is None or not data.get("success", True):
                raise FetchFailedException()
        except json.decoder.JSONDecodeError as e:
            raise FetchFailedException()

        return data

    async def get_inverter_details(self, inverter_sn: str) -> dict:
        """
        Get PV inverter details from 2 sources
        :param inverter_sn: PV inverter serial number (can be found in deviceList)
        :raises:
            FetchFailedException: failed to fetch data from endpoint
        :return: dict("d1": dict, "d2": dict)
        """
        response = await self.client.get(self.get_url("newInverterAPI.do"), params={
            "op": "getInverterDetailData",
            "inverterId": inverter_sn
        })
        try:
            d1 = json.loads(response.content.decode("utf-8"))
        except json.decoder.JSONDecodeError as e:
            raise FetchFailedException()

        response = await self.client.get(self.get_url("newInverterAPI.do"), params={
            "op": "getInverterDetailData_two",
            "inverterId": inverter_sn
        })
        try:
            d2 = json.loads(response.content.decode("utf-8"))
        except json.decoder.JSONDecodeError as e:
            raise FetchFailedException()

        return {"d1": d1, "d2": d2}

    async def get_dashboard_data(self, plant_id: str, timespan: Timespan = Timespan.HOUR,
                                 date: datetime.date = None) -> dict:
        """
        Get dashboard data for given timespan and date
        :param plant_id: plant ID
        :param timespan: Timespan value (defaults to Timespan.HOUR)
        :param date: start date (defaults to today)
        :raises:
            FetchFailedException: failed to fetch data from endpoint
        :return:
            dict(
                "echargeToat": str,
                "photovoltaic": str,
                "eCharge": str,
                "eAcCharge": str,
                "elocalLoad": str,
                "keyNames": [],
                "eChargeToday2Echarge1": str,
                "chartData": {
                    "ppv": list of strs depending on the Timespan value given,
                    "sysOut": list of strs depending on the Timespan value given,
                    "userLoad": list of strs depending on the Timespan value given,
                    "pacToUser": list of strs depending on the Timespan value given
                },
                "etouser": str,
                "ratio2": str,
                "ratio1": str,
                "echarge1": str,
                "eChargeToday2": str,
                "ratio4": str,
                "ratio3": str,
                "chartDataUnit": str,
                "ratio6": str,
                "eChargeToday1": str,
                "ratio5": str
            )
        """
        date_str = date_to_str(timespan, date)

        response = await self.client.post(self.get_url('newPlantAPI.do'), params={
            "action": "getEnergyStorageData",
            "date": date_str,
            "type": timespan.value,
            "plantId": plant_id
        })
        try:
            data = json.loads(response.content.decode("utf-8"))
            if data is None or not data.get("success", True):
                raise FetchFailedException()
        except json.decoder.JSONDecodeError as e:
            raise FetchFailedException()

        return data

    async def get_tlx_data(self, tlx_inverter_sn: str, date: datetime.date = None) -> dict:
        """
        Get TLX inverter data for specified date (defaults to today).
        :param tlx_inverter_sn: TLX inverter serial number
        :param date: specific date (defaults to today)
        :raises:
            FetchFailedException: failed to fetch data from endpoint
        :return: dict of TLX inverter data
        """
        date_str = date_to_str(date=date)
        response = await self.client.get(self.get_url("newTlxApi.do"), params={
            "op": "getTlxData",
            "id": tlx_inverter_sn,
            "type": 1,
            "date": date_str
        })
        try:
            data = json.loads(response.content.decode("utf-8"))
            if data is None or not data.get("success", True):
                raise FetchFailedException()
        except json.decoder.JSONDecodeError as e:
            raise FetchFailedException()

        return data

    async def get_tlx_details(self, tlx_inverter_sn: str) -> dict:
        """
        Get all TLX inverter details for a specific date
        :param tlx_inverter_sn: TLX inverter serial number
        :raises:
            FetchFailedException: failed to fetch data from endpoint
        :return: dict of TLX inverter details
        """
        response = await self.client.get(self.get_url("newTlxApi.do"), params={
            "op": "getTlxDetailData",
            "id": tlx_inverter_sn
        })
        try:
            data = json.loads(response.content.decode("utf-8"))
            if data is None or not data.get("success", True):
                raise FetchFailedException()
        except json.decoder.JSONDecodeError as e:
            raise FetchFailedException()

        return data

    async def get_mix_info(self, mix_inverter_sn: str, plant_id: str = None) -> dict:
        """
        Get high-level information of MIX inverter
        :param mix_inverter_sn: MIX inverter serial number
        :param plant_id: plant ID
        :raises:
            FetchFailedException: failed to fetch data from endpoint
        :return: dict of MIX inverter information
        """
        request_params = {
            "op": "getMixInfo",
            "mixId": mix_inverter_sn
        }

        if plant_id is not None:
            request_params["plantId"] = plant_id

        response = await self.client.get(self.get_url("newMixApi.do"), params=request_params)
        try:
            data = json.loads(response.content.decode("utf-8"))["obj"]
            if data is None or not data.get("success", True):
                raise FetchFailedException()
        except json.decoder.JSONDecodeError as e:
            raise FetchFailedException()

        return data

    async def get_mix_today_total(self, mix_inverter_sn: str, plant_id: str) -> dict:
        """
        Get today's total values for MIX inverter
        :param mix_inverter_sn: MIX inverter serial number
        :param plant_id: plant ID
        :raises:
            FetchFailedException: failed to fetch data from endpoint
        :return: dict of today's total values
        """
        response = await self.client.post(self.get_url("newMixApi.do"), params={
            "op": "getEnergyOverview",
            "mixId": mix_inverter_sn,
            "plantId": plant_id
        })
        try:
            data = json.loads(response.content.decode("utf-8"))["obj"]
            if data is None or not data.get("success", True):
                raise FetchFailedException()
        except json.decoder.JSONDecodeError as e:
            raise FetchFailedException()

        return data

    async def get_mix_status(self, mix_inverter_sn, plant_id):
        """
        Get MIX inverter's current status
        :param mix_inverter_sn: MIX inverter serial number
        :param plant_id: plant ID
        :raises:
            FetchFailedException: failed to fetch data from endpoint
        :return: dict of MIX inverter status
        """
        response = await self.client.post(self.get_url("newMixApi.do"), params={
            "op": "getSystemStatus_KW",
            "mixId": mix_inverter_sn,
            "plantId": plant_id
        })
        try:
            data = json.loads(response.content.decode("utf-8"))["obj"]
            if data is None or not data.get("success", True):
                raise FetchFailedException()
        except json.decoder.JSONDecodeError as e:
            raise FetchFailedException()

        return data

    async def get_mix_details(self, mix_inverter_sn: str, plant_id: str, timespan: Timespan = Timespan.HOUR,
                              date: datetime.date = None) -> dict:
        """
        Get MIX inverter details for specified timespan and date
        :param mix_inverter_sn: MIX inverter serail number
        :param plant_id: plant ID
        :param timespan: Timespan (defaults to Timespan.HOURS)
        :param date: specific date (defaults to today)
        :raises:
            FetchFailedException: failed to fetch data from endpoint
        :return: dict of MIX inverter details
        """
        date_str = date_to_str(timespan, date)

        response = await self.client.post(self.get_url("newMixApi.do"), params={
            "op": "getEnergyProdAndCons_KW",
            "plantId": plant_id,
            "mixId": mix_inverter_sn,
            "type": timespan.value,
            "date": date_str
        })
        try:
            data = json.loads(response.content.decode("utf-8"))["obj"]
            if data is None or not data.get("success", True):
                raise FetchFailedException()
        except json.decoder.JSONDecodeError as e:
            raise FetchFailedException()

        return data
