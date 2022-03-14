# SmartMeetingRoom
本智能会议室管理系统旨在将虹软人工智能平台与物联网智能硬件技术相结合，开发出一套能够满足绝大部分应用场景的人性化、智能化、自动化的会议室管理系统，为用户提供良好体验。
基本技术目标包括：
（1）基于虹软人工智能平台开发设计
（2）支持多个会议及会议室管理，及多人同时预定
（3）支持人脸门禁会议、签到打卡
（4）系统易用、可拓展、人性化、智能化
（5）硬件成本适宜

应用环境：
网页客户端：Edge、火狐、谷歌等浏览器

微信端用户：微信客户端2.6.2及以上版本

会议室端：带前置摄像头平板、stm32f4或其他嵌入式系列开发板

功能需求概述
会议室查询
在网页端和微信端，可预览所有会议室及排期情况；查询预定满足条件的会议室。
会议室预定
1.	线下预定
可在网页端、微信端登陆后，填写会议的详细信息后，对空闲时段的会议室进行预定或修改。
2.	线下预定
在会议室门口处，操作平板对此会议室进行预定；打开微信端的扫一扫，对会议室门口处的二维码进行扫描后亦可预定。
人脸门禁
在会议室前端配备平板，通过人脸核验才可开启电磁锁门禁。
签到打卡
与会者通过人脸核验后系统自动签到打卡，可在前端查看。
会议室管理
增删人员信息，录入人员的照片信息；对会议室的异常情况进行处理。
会议提醒
1.开始提醒
与微信小程序关联的公众号会在会议预定后，通知所有的与会者，并会发送短信；
在会议开始15分钟前，再次提醒，以免迟到。
2.结束提醒
距会议结束时间5分钟，提醒预定者按时结束会议。
智能调度
根据预定者输入的参会信息，使用智能调度算法，智能推荐匹配会议室。
环境检测
会议室内部单片机系统通过摄像头监测室内环境，在非会议时段检测到会议室内无人时控制断电关闭门禁。
条件与限制
系统使用的条件与限制主要有：除了离线功能外，本作品的客户端功能均需要连接系统的服务器。
设计原则
    智能会议室系统系统设计遵循以下原则：
（1）良好的用户界面
（2）操作简便性
（3）系统可拓展性
（4）人性化、自动化设计
（5）硬件成本适宜
（6）快速性，人脸门禁核验速率达到使用要求
设计思想
良好的用户界面可以极大地提高用户的使用体验，前端界面设计尽量简洁大方，并保持一致的审美效果。
为了使系统操作简便，设计中模块分区合理，符合用户的使用习惯，并显示提示语言与用户进行人机交互。
为了使系统功能具有一定的可拓展性，采用分层模式的思想，将系统分为三层：数据层、逻辑层、表现层。对于可能变化的文件内容，系统只需要修改数据层与数据库的交互代码即可，无需改动逻辑层和表现层。
采用虹软人脸识别技术使得人脸门禁核验快速准确，满足绝大部分应用场景使用需求。
通过拓展虹软人脸识别技术，将其衍生应用于室内环境监测，使系统更加智能化、人性化。
示。

分模块设计
智会系统主要包括Web客户模块、微信用户模块、后台管理模块和会议室前端模块。
（1）Web客户模块中，普通用户可以根据公司给定的工号和初始密码进行登录，同时第一次登录后需要绑定微信号。用户可以通过访问Web端预定界面查看个人即将参加的会议、创建的会议、已经参加的会议等。同时可以预览公司所有会议室详情按照自己的喜好选择指定的空闲会议室，也可以通过指定会议时间并通过智能匹配最佳会议室。

（2）微信用户模块中，用户通过预先网页端登录时绑定的微信号登录小程序，即可实现查询、预定、修改会议室等功能，并可以直接在小程序上发起会议。在会议预定成功后，小程序关联的公众号会给用户发来会议提醒，同时在会议召开前半个小时还会再发送一次会议提醒，防止用户遗忘，并且在会议结束前10分钟会发来会议即将结束的信息，防止影响下一场会议的召开。

（3）后台管理模块部分提供基于Web端的会议室后台管理系统，我们使用了HTML5+CSS3+JavaScript，Bootstrap框架，Jquery构建前端。管理员身份信息一开始就被注册到数据库当中，管理员通过初始账号和密码登录管理员端后可以对使用人员进行管理、人脸注册等功能，具体包括对公司部门进行增删改查，对员工ID、所属部门等个人信息进行增删改查，对会议室编号、硬件设施等进行编辑，同时对申请发起的会议进行实时审核功能。
管理员可以通过部门管理对部门信息进行修改，同时结合快速搜索功能方便管理员操作，员工管理可以对员工照片、姓名、归属部门、电话以及绑定的微信号进行编辑。同时管理员可以及时的对会议室的硬件设施情况进行实时编辑。

（4）会议室前端通过放置平板，在平板上滚动播放当前会议室的预定情况，同时提供刷脸签到和实时预定功能，用户可以通过查看会议室当前预定情况后选择该会议室的空余时间进行预定，同时也可以通过微信小程序扫描该会议室的二维码进行预定。


Web客户端
![image](https://user-images.githubusercontent.com/30195788/158125662-c167fcbb-0da9-4891-b309-69bb6da78579.png)
![image](https://user-images.githubusercontent.com/30195788/158125673-5e30ba3c-2806-462d-a420-f8c28ed0b737.png)
![image](https://user-images.githubusercontent.com/30195788/158125682-015fda2e-e267-4aae-83b7-bde33ccf9434.png)
![image](https://user-images.githubusercontent.com/30195788/158125696-70a97bb1-7171-4a93-a79b-c5199ff11299.png)
![image](https://user-images.githubusercontent.com/30195788/158125718-f2222b0d-f287-4fdc-9b5b-1b64a9bdf0a9.png)
![image](https://user-images.githubusercontent.com/30195788/158125736-8d22388e-41e5-4e7f-8629-b26c416c6015.png)
![image](https://user-images.githubusercontent.com/30195788/158125755-a9a3f444-3aff-48dd-a91e-67b1a52d3cf7.png)
![image](https://user-images.githubusercontent.com/30195788/158125776-47f57635-8c50-4de2-a943-05b206a4534c.png)


微信用户端
![image](https://user-images.githubusercontent.com/30195788/158125743-6d4e605a-a8c7-404c-a2d4-ba88136c526a.png)
 ![image](https://user-images.githubusercontent.com/30195788/158125791-da2448d4-4cfa-40de-aef6-2e7d7e27e598.png)
 ![image](https://user-images.githubusercontent.com/30195788/158125818-83ed457f-8484-47f6-9e10-e7eee937704c.png)
   ![image](https://user-images.githubusercontent.com/30195788/158125832-e69e6d7b-41af-4c15-92db-d89520b1a115.png)
![image](https://user-images.githubusercontent.com/30195788/158125844-9366ed26-4807-4e4a-b046-30b7f6a2e7ba.png)
![image](https://user-images.githubusercontent.com/30195788/158125857-c9a8e0de-e144-49da-a3fe-1e8ea9d70f5d.png)
![image](https://user-images.githubusercontent.com/30195788/158125896-c0fadf8b-ea04-4cb9-8449-a3c3df745a3c.png)


会议室前端
 ![image](https://user-images.githubusercontent.com/30195788/158125977-aa22da52-0d3d-4197-9501-c3eea072ede3.png)
![image](https://user-images.githubusercontent.com/30195788/158126012-dcf55cef-94ae-4018-a2f4-67129cc76bc6.png)
![image](https://user-images.githubusercontent.com/30195788/158126030-e93f409e-2f3f-4e4c-8a4c-138992a58d3c.png)


数据库设计
数据库描述
数据表列表
序号	名称	描述
1	app_department	部门表存储部门的名称，id
2	app_meeting	会议表存储会议的id、创建人、名称、会议日期、开始时间、结束时间、与会人员
3	app_meetingroom	会议室表存储会议室的id、名称、设备、概貌、容纳人数
4	app_staff	职工表存储员工的id、工号、名称、照片
5	app_sudo	Sudo存储当前时段与会人员面部信息
6	app_userinfor	Userinfo表存储摄像头检测识别的人脸信息
7	auth_user	存储员工密码、是否为管理员、id

物理结构设计
1、用户信息表（auth_user）
字段	说明	类型	可空	备注
User_id	id	int	NO	主键，自增
User_name	名称	varchar	YES	
pwd	密码	char	YES	


2、检测信息表（auth_userinfo）
字段	说明	类型	可空	备注
Info_id	id	int	NO	主键，自增
Info_data	面部数据	Longtext	YES	人脸数据
Info_state	状态	Int	YES	更新状态


3、与会人员信息表（app_sudo）
字段	说明	类型	可空	备注
Sudo_id	id	int	NO	主键，自增
Sudo_name	名称	varchar	YES	
Sudo_data	面部数据	Longtext	YES	
Sudo_number	工号	int	YES	


4、全体员工信息表（app_staff）
字段	说明	类型	可空	备注
Staff_id	工号	int	NO	主键
Staff_name	姓名	varchar	YES	
Staff_image	照片	longtext	YES	
Staff_sex	性别	char	YES	
Staff_job	职业	varchar	YES	
表5.3.4全体员工信息表

5、会议室信息表（app_meetingroom）
字段	说明	类型	可空	备注
Room_id	id	int	NO	主键，自增
Room_name	名称	varchar	YES	
Room_number	容纳人数	Int	YES	
Room_shebei	设备	Longtext	YES	
表5.3.5会议室信息表

6、会议信息（app_meeting）
字段	说明	类型	可空	备注
Meet_id	id	int	NO	主键，自增
Meet_name	会议名称	varchar	YES	
Meet_owner	发起人	varchar	YES	
Meet_data	会议日期	char	YES	
Meet_btime	开始时间	char	YES	
Meet_etime	结束时间	char	YES	

7、部门表(app_department）
字段	说明	类型	可空	备注
Dt_id	id	int	NO	主键，自增
Dt_name	名称	varchar	YES	

