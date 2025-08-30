# B站API接入指南

本文档将指导您如何在项目中接入真实的B站API，替换当前使用的模拟数据。

## 前置准备

要接入B站API，您需要完成以下准备工作：

### 1. 个人开发者和企业开发者说明

B站开放平台目前主要面向企业开发者，但个人开发者仍有替代方案可以接入B站内容。

**对于个人开发者：**
- 您可以使用B站提供的[个人开发者认证](https://member.bilibili.com/platform/apply-personal)
- 如果无法通过企业认证，还可以考虑使用B站分享功能生成的嵌入代码
- 或者使用第三方API服务（需要注意遵守B站的使用条款）

**对于企业开发者：**
1. 访问 [B站开放平台](https://open.bilibili.com/)
2. 注册并登录开发者账号
3. 创建新应用，获取 `client_id` 和 `client_secret`
4. 设置应用的回调地址（Redirect URI）

### 2. 了解B站API认证机制

B站API使用OAuth2.0认证机制，主要流程如下：

1. 用户授权：引导用户访问授权页面
2. 获取授权码：用户授权后，B站会重定向到您设置的回调地址，并带上授权码
3. 获取访问令牌：使用授权码换取访问令牌（access_token）
4. 调用API：使用访问令牌调用B站API

## 后端实现

### 1. 个人开发者替代方案

是的，个人开发者完全可以直接提供BV号来展示视频！由于B站API对个人开发者的限制，您可以采用以下方案，直接在后端硬编码您的视频信息：

```python
# backend/creative_lab/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_bilibili_videos_personal(request):
    try:
        # 对于个人开发者，可以直接在这里硬编码您的视频信息
        # 当您上传新视频时，手动更新这个列表
        videos = [
            {
                'bvid': 'BV1Ei4y1w7R7',  # 您提供的第一个视频BV号
                'title': '【我想吃掉你的胰脏】生命是有光的，至少在我熄灭之后，能照亮你一点也是我所能做的了……',
                'description': '分享我对《我想吃掉你的胰脏》的理解与感悟，生命的意义在于照亮他人。',
                'cover': 'https://via.placeholder.com/480x270?text=我想吃掉你的胰脏',  # 视频封面图
                'duration': 360,  # 视频时长（秒），您可以根据实际视频时长调整
                'viewCount': '1.2万',  # 观看数量，您可以根据实际情况更新
                'publishDate': '2023-12-15'  # 发布日期
            },
            {
                'bvid': 'BV1d54y167NB',  # 您提供的第二个视频BV号
                'title': '估计只有真正喜欢国家队的才能刷到这个视频吧~',
                'description': '国家队粉丝专属内容，重温那些感动瞬间。',
                'cover': 'https://via.placeholder.com/480x270?text=国家队专题',  # 视频封面图
                'duration': 480,  # 视频时长（秒）
                'viewCount': '8.5千',  # 观看数量
                'publishDate': '2024-01-20'  # 发布日期
            }
            # 您可以继续添加更多视频
        ]
        
        return Response(videos)
    except Exception as e:
        print(f'Error fetching bilibili videos: {e}')
        return Response({'error': 'Failed to fetch videos'}, status=500)
```

### 2. 企业开发者API代理方案

如果您是企业开发者或已获得API访问权限，可以使用以下方案：

```python
# backend/creative_lab/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import os

@api_view(['GET'])
def get_bilibili_videos(request):
    # 这里应该从安全的地方获取访问令牌
    # 在实际项目中，您可能需要实现完整的OAuth2.0流程
    access_token = request.GET.get('access_token', '')
    
    if not access_token:
        return Response({'error': 'Missing access token'}, status=400)
    
    try:
        # 调用B站API获取视频列表
        # 这里使用的是示例API，实际使用时需要参考B站API文档
        url = 'https://api.bilibili.com/x/space/wbi/arc/search'
        params = {
            'mid': 'YOUR_BILIBILI_UID',  # 替换为您的B站用户ID
            'ps': 20,  # 每页视频数量
            'pn': 1,   # 页码
            'jsonp': 'jsonp'
        }
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        
        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        
        # 处理B站API返回的数据，转换为前端需要的格式
        videos = []
        if data.get('code') == 0 and data.get('data'):
            for item in data['data']['list']['vlist']:
                videos.append({
                    'bvid': item.get('bvid'),
                    'title': item.get('title'),
                    'description': item.get('description'),
                    'cover': item.get('pic'),
                    'duration': item.get('length'),
                    'viewCount': item.get('play'),
                    'publishDate': item.get('created')
                })
        
        return Response(videos)
    except Exception as e:
        print(f'Error fetching bilibili videos: {e}')
        return Response({'error': 'Failed to fetch videos'}, status=500)
```

```python
# backend/creative_lab/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import os

@api_view(['GET'])
def get_bilibili_videos(request):
    # 这里应该从安全的地方获取访问令牌
    # 在实际项目中，您可能需要实现完整的OAuth2.0流程
    access_token = request.GET.get('access_token', '')
    
    if not access_token:
        return Response({'error': 'Missing access token'}, status=400)
    
    try:
        # 调用B站API获取视频列表
        # 这里使用的是示例API，实际使用时需要参考B站API文档
        url = 'https://api.bilibili.com/x/space/wbi/arc/search'
        params = {
            'mid': 'YOUR_BILIBILI_UID',  # 替换为您的B站用户ID
            'ps': 20,  # 每页视频数量
            'pn': 1,   # 页码
            'jsonp': 'jsonp'
        }
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        
        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        
        # 处理B站API返回的数据，转换为前端需要的格式
        videos = []
        if data.get('code') == 0 and data.get('data'):
            for item in data['data']['list']['vlist']:
                videos.append({
                    'bvid': item.get('bvid'),
                    'title': item.get('title'),
                    'description': item.get('description'),
                    'cover': item.get('pic'),
                    'duration': item.get('length'),
                    'viewCount': item.get('play'),
                    'publishDate': item.get('created')
                })
        
        return Response(videos)
    except Exception as e:
        print(f'Error fetching bilibili videos: {e}')
        return Response({'error': 'Failed to fetch videos'}, status=500)
```

### 3. 在后端配置URL路由

```python
# backend/creative_lab/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 其他URL配置
    # 个人开发者方案
    path('api/bilibili/videos-personal/', views.get_bilibili_videos_personal, name='get_bilibili_videos_personal'),
    # 企业开发者方案
    path('api/bilibili/videos/', views.get_bilibili_videos, name='get_bilibili_videos'),
]
```

## 前端实现

### 1. 修改CreativeLab.vue中的loadVideos方法（个人开发者方案）

```javascript
// 个人开发者版本
async loadVideos() {
  try {
    this.loadingVideos = true;
    
    // 调用后端为个人开发者提供的API端点
    const response = await api.get('/api/bilibili/videos-personal');
    this.videos = response.data;
  } catch (error) {
    console.error('加载视频失败:', error);
    // 显示错误提示给用户
    this.$message.error('加载视频失败，请稍后重试');
    
    // 加载失败时使用备用的模拟数据
    this.useMockVideos();
  } finally {
    this.loadingVideos = false;
  }
}

// 企业开发者版本（原有代码）
async loadVideos() {
  try {
    this.loadingVideos = true;
    
    // 调用后端代理的B站API
    const response = await api.get('/api/bilibili/videos');
    
    // 处理返回的视频数据
    this.videos = response.data.map(video => ({
      ...video,
      // 格式化日期（如果需要）
      publishDate: this.formatDateFromTimestamp(video.publishDate)
    }));
  } catch (error) {
    console.error('加载视频失败:', error);
    // 显示错误提示给用户
    this.$message.error('加载视频失败，请稍后重试');
    
    // 加载失败时使用备用的模拟数据
    this.useMockVideos();
  } finally {
    this.loadingVideos = false;
  }
},

// 从时间戳格式化日期
formatDateFromTimestamp(timestamp) {
  const date = new Date(timestamp * 1000);
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
},

// 使用模拟数据作为备用
useMockVideos() {
  this.videos = [
    {
      bvid: 'BV1EX4y1w7sL',
      title: '【前端开发】Vue3 + Vite 项目实战教程',
      description: '本视频详细讲解了如何使用Vue3 + Vite构建现代化前端项目',
      cover: 'https://via.placeholder.com/480x270?text=Vue3+Vite',
      duration: 1260,
      viewCount: '2.4万',
      publishDate: '2023-05-15'
    },
    // 其他模拟数据...
  ];
}
```

### 2. 个人开发者简化版实现

对于个人开发者，您可以跳过复杂的OAuth2.0授权流程，直接使用以下简化实现：

```javascript
// 在CreativeLab.vue中实现
// 1. 手动管理视频列表（在后端或前端）
// 2. 直接跳转到B站观看视频

// 此方法已在之前的实现中包含
playVideo(video) {
  // 在新标签页打开B站视频
  window.open(`https://www.bilibili.com/video/${video.bvid}`, '_blank');
}

// 或者，您可以使用B站的嵌入功能在页面内播放视频
// 在template中添加一个模态框
// <div v-if="selectedVideo" class="video-modal" @click="closeVideoModal">
//   <div class="video-modal-content" @click.stop>
//     <button class="close-btn" @click="closeVideoModal">×</button>
//     <iframe 
//       :src="selectedVideoEmbedUrl" 
//       frameborder="0" 
//       allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
//       allowfullscreen
//       class="video-player"
//     ></iframe>
//   </div>
// </div>

// 在script中添加相关属性和方法
// data() {
//   return {
//     // 其他属性...
//     selectedVideo: null,
//   }
// },

// computed: {
//   selectedVideoEmbedUrl() {
//     if (!this.selectedVideo) return '';
//     return `https://player.bilibili.com/player.html?bvid=${this.selectedVideo.bvid}&page=1`;
//   }
// },

// methods: {
//   // 其他方法...
//   playVideoInPage(video) {
//     this.selectedVideo = video;
//     // 阻止背景滚动
//     document.body.style.overflow = 'hidden';
//   },
//   
//   closeVideoModal() {
//     this.selectedVideo = null;
//     // 恢复背景滚动
//     document.body.style.overflow = '';
//   }
// }
```

## 安全注意事项和使用条款

### 对于企业开发者：

1. **不要在前端暴露敏感信息**：`client_secret`等敏感信息应妥善保管在后端
2. **使用HTTPS**：确保所有API通信都通过HTTPS进行
3. **保护访问令牌**：访问令牌应存储在安全的地方，避免被恶意获取
4. **实现令牌刷新机制**：B站的访问令牌有有效期，需要实现自动刷新机制
5. **限制API请求频率**：遵守B站API的调用频率限制，避免被封禁

### 对于个人开发者：

1. **遵守B站使用条款**：确保您的使用方式符合B站的[用户协议](https://www.bilibili.com/blackboard/activity-kycg2021.html)和[内容创作公约](https://www.bilibili.com/blackboard/activity-guild2020.html)
2. **不要滥用API**：即使使用个人开发者替代方案，也不要进行过度请求或滥用B站资源
3. **正确归因**：在展示B站视频内容时，确保正确标注来源并提供原始链接
4. **定期更新视频信息**：由于是手动维护视频列表，请记得在上传新视频后更新相关信息

## 调试和测试

1. 使用B站提供的[API调试工具](https://api.bilibili.com/dev-tool/console)进行测试
2. 在开发环境中使用模拟数据和真实API进行对比测试
3. 添加适当的错误处理和日志记录
4. 测试不同网络环境下的加载性能

## 参考资源

- [B站开放平台文档](https://open.bilibili.com/doc)
- [OAuth2.0官方文档](https://oauth.net/2/)
- [Django REST Framework文档](https://www.django-rest-framework.org/)
- [Axios文档](https://axios-http.com/docs/intro)