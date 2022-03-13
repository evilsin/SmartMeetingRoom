/**
 * @file scan.js
 * @author xuguixin0624@gmail.com
 * @description 会议室排期详情
 */
import Util from "../../utils/util.js";
import API from "../../api/api.js";
var app = getApp();
Page({
	data: {
		brDetailsList: {
      "name": "B219会议室排期",
      "id": "11",
      "array": [
        { "start_time": "9:00", "end_time": "10:30", "title": "关于人事调动会议", "initiator": "侯晓妍" },
        { "start_time": "16:00", "end_time": "17:00", "title": "关于开发部大会", "initiator": "张艺兴" },
        { "start_time": "17:00", "end_time": "17:50", "title": "公司年会", "initiator": "陆建华" }
      ]
    },
		title: ''
	},
	onLoad (options) {
    wx.setNavigationBarTitle({
      title: this.data.brDetailsList.name
    });
	}
})
