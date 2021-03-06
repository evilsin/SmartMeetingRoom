import API from "../../api/api.js";
var app = getApp();
Page({
  onLoad (){
    // 生命周期函数--监听页面加载
    var meetingroomsTemp = [{ id: 'one', name: 'A201', initial: 'A区' }, { id: 'two', name: '第二会议室', initial: '北京' }, { id: 'two', name: '深圳会议室', initial: '深圳' }, { id: 'two', name: '广州会议室', initial: '广州' }];
    app.updateMeetingrooms(meetingroomsTemp);
  },
  scan() {
    //扫码事件
    wx.scanCode({
      success: function(res) {
        wx.navigateTo({
          url: "../scan/scan"
        })
      },
      fail: function(res) {
        wx.showToast({
          title: '扫码失败',
          image: '../../images/failmsg.png',
          duration: 2000
        })
      }
    })
  }, 
  local() {
    wx.navigateTo({
      url: "../local/local"
    })
  },
  reserve() {
    wx.navigateTo({
      url: "../reserve/reserve"
    });
  },
  schedule() {
    wx.navigateTo({
      url: "../schedule/schedule"
    })
  }
})
