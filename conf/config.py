#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/29 下午9:03
# @Author  : Hou Rong
# @Site    : 
# @File    : config.py
# @Software: PyCharm


# TaskServer
server_port = 8087

# TaskDB
mongo_host = 'mongodb://root:miaoji1109-=@10.19.2.103:27017/'
mongo_base_task_db = 'RoutineBaseTask'
mongo_date_task_db = 'RoutineDateTask'

test_mongo_date_task_db = 'Test_RoutineDateTask'
# hotel_base_task_db = 'HotelRoutineBaseTask'

# TaskCollection
package_info_collection = 'package_info'

per_retrieve_count = 200

used_times_config = 2 #包括第一次