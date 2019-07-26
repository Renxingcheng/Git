git
什么是git?
  分布式版本控制系统                            
  git的诞生
    linux linus
分布式和集中式
git:安装
设置名字
 git config --global user.name "rxc"   （#*）
设置邮箱
 git config --global user.email "295058621@qq.com"    （#*）
创建版本库：（制定目录为版本库）
          创建一个空目录，作为版本库
          初始化版本库：
                      1.进入版本库所在目录
                      2.执行初始化命令
                        git init
管理内容：
         文本，代码，网页 .txt.c.java.html
把文件添加到版本库：
                    1.创建一个文件
                    2.在仓库里面查看状态   #先查看文件状态
                      git status
                    3.把文件添加到版本库   #查看过后把创建的文件 放进版本库里面
                      git add （+文件名）
                    4.把文件提交给版本库   #文件放进版本库后 告诉版本库文件的信息 才能记录修改记录和管理
                      git commit -m "信息"
                    5.查看文件每个版本
                      git log
时光穿梭：（回到以前版本）
        git reset --hard HEAD（+版本）
                  版本 写法：
                  HEAD:代表当前版本
                  HEAD^:代表上一个版本
                  HEAD~100:代表上100个版本
        后悔药：（回到现在版本）
              git reflog:查看历史所有版本
              git reset --hard (+版本号)
文件修改撤销：
             git checkout -- (文件名)

场景：
    1.在未提交之前，撤销修改
      git checkout -- (文件名)
    2.在文件提交到暂存区，撤销修改
       清除暂存区的文件
      git reset HEAD （文件名）
      替换工作区文件
      git checkout -- （文件名）
    3.在文件已经被commit之后，撤销修改，版本回退。 
  删除文件
         不想删除：git checkout -- (文件名)  （误删）


         真想删除：（传达指令的过程）
                  1.删除源文件
                  2.添加暂存区（源文件）
                   git add （文件名）
                  3.提交
                   git commit -m "信息" 


(联机的git)
Github:



https://github.com/Renxingcheng/Git.git  网站传输地址
SSH:git@github.com:Renxingcheng/Git.git  加密传输网址


将本机的SSH（加密传输）添加到github：
      1.在本地创建SSH key
       ssh-keygen -t rsa -C(大写) "email"
      2.找到SSH key 所在的地方
        （默认c://user/用户名/.ssh)
      3.复制 .ssh /  id_rsa.pub 的内容 放到网站。
      4.测试是否能够连接成功
        ssh -T(大写) git@github.com


把本地仓库上传到远程github：
        1.本地和远程连接
          git remote add origin +远程仓库的地址 
        2.把本地仓库推送到远程
          git push -u origin master #(第一次推送使用)
          git push  origin master
把远程仓库克隆到本地
        1.git clone +地址
协同开发：
        1.添加好友的ssh key
        2.添加git好友 
参加开源项目：
            1.先找到要参加的开源的项目，fork到自己的网络仓库（github）
            2.把自己fork的项目clone到本地
            3.修改项目
            4.把修改好的项目push到自己的github仓库
            5.把自己的修改pull给作者

        