#
用户model使用了django contrib.auth提供的auth-user   
使用drf的APIView,Serializers, permissions, status  
使用jwt生成token    

#API
    注册用户    
    http://127.0.0.1:8000/api/v1/auth/register/
    获取用户token   
    http://127.0.0.1:8000/api-token-auth/
    用户登录
    http://127.0.0.1:8000/api/v1/auth/login/

    获取/添加歌曲列表
    http://127.0.0.1:8000/api/v1/songs
    获取/更新/删除歌曲信息
    http://127.0.0.1:8000/api/v1/songs/3/