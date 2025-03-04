def mainPage_sidebar(
    avatar: str,
    name: str,
    description: str,
    social_links: dict,
    tag_cloud: dict
):
    """
    侧边栏
    :param avatar: 头像URL
    :param name: 站长名
    :param description: 站长身份
    :param social_links: 社交链接，传入嵌套后的字典，如： `{"Github": ["https://github.com/Yuerchu", "fab fab-github"]]}`
    :param tag_cloud: 标签云字典
    """

    # 社交账号拼接
    social_links_html = ""
    if social_links: 
        for title, param in social_links.items():
            social_links_html += f'<a href="{param[0]}" title="{title}"><i class="{param[1]}"></i></a>'
    
    # 标签云拼接
    tag_cloud_html = ""
    if tag_cloud: 
        for title, url in tag_cloud.items():
            tag_cloud_html += f'<a href="{url}" class="tag">{title}</a>'

    return f"""
    <aside class="sidebar">
        <div class="sidebar-widget about-widget">
            <div class="avatar">
                <img src="{avatar}" alt="avatar">
            </div>
            <h3>{name}</h3>
            <p>{description}</p>
            <div class="social-links">
                {social_links_html}
            </div>
        </div>
        
        <!-- 热门文章 -->
        <div class="sidebar-widget">
            <h3 class="widget-title"><i class="fas fa-fire"></i> 热门文章</h3>
            <div class="popular-posts">
                <a href="#" class="popular-post">
                    <img src="https://via.placeholder.com/60x60" alt="热门文章">
                    <div>
                        <h4>原创漫画创作指南：从构思到发布</h4>
                        <span><i class="far fa-eye"></i> 2356</span>
                    </div>
                </a>
                <a href="#" class="popular-post">
                    <img src="https://via.placeholder.com/60x60" alt="热门文章">
                    <div>
                        <h4>漫画网站流量提升的十个实用策略</h4>
                        <span><i class="far fa-eye"></i> 1897</span>
                    </div>
                </a>
                <a href="#" class="popular-post">
                    <img src="https://via.placeholder.com/60x60" alt="热门文章">
                    <div>
                        <h4>动漫角色设计的心理学解析</h4>
                        <span><i class="far fa-eye"></i> 1682</span>
                    </div>
                </a>
            </div>
        </div>
        
        <!-- 标签云 -->
        <div class="sidebar-widget">
            <h3 class="widget-title"><i class="fas fa-tags"></i> 标签云</h3>
            <div class="tag-cloud">
                {tag_cloud_html}
            </div>
        </div>
        
        <!-- 订阅框 -->
        <div class="sidebar-widget subscribe-widget">
            <h3 class="widget-title"><i class="fas fa-envelope"></i> 订阅更新</h3>
            <p>输入邮箱获取最新文章和资源推送</p>
            <form class="subscribe-form">
                <input type="email" placeholder="您的邮箱地址" required>
                <button type="submit" class="btn primary">订阅</button>
            </form>
        </div>
    </aside>
    """