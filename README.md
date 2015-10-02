#安装（平台级别的设置）
<pre>
sudo su edxapp -s /bin/bash
cd ~
source edxapp_env
pip install -e git+https://github.com/lovehhf/polyvXBlock#egg=polyvXBlok
exit
sudo /edx/bin/supervisorctl restart edxapp:
</pre>
在/edx/app/edxapp/cms.env.json 添加 `"ALLOW_ALL_ADVANCED_COMPONENTS": true,` 到FEATURES


#在studio中设置(课程级别的设置)
进入到"Settings" ⇒ "Advanced Settings",将"youku"添加到Advanced Module List
