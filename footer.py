def footer(
    left_title: str,
    left_description: str,
    fast_link: dict,
    friend_link: dict,
    connect: dict,
    email: str,
    qq_group: str,
    weibo: str,
    bilibili: str,
    twitter: str,
    footer_bottom: list
):
    # 快速链接生成HTML
    fast_link_html = ""
    for name, url in fast_link.items():
        fast_link_html += f'<li><a href="{url}">{name}</a></li>\n'

    # 友情链接生成HTML
    friend_link_html = ""
    for name, url in friend_link.items():
        friend_link_html += f'<li><a href="{url}" target="_blank">{name}</a></li>'
    
    # 联系我生成HTML
    connect_link_html = ""
    for name, url in connect.items():
        connect_link_html += f'<li><a href="{url}" target="_blank">{name}</a></li>'
    
    # 最底部的信息
    footer_bottom_html = ""
    for items in footer_bottom:
        footer_bottom_html += f'<p>{items}</p>'

    return f"""
    <footer class="footer">
        <div class="footer-top">
            <div class="container">
                <div class="footer-widgets">
                    <div class="footer-widget">
                        <h4>{left_title}</h4>
                        <p>{left_description}</p>
                    </div>
                    <div class="footer-widget">
                        <h4>快速链接</h4>
                        <ul class="footer-links">
                            {fast_link_html}
                        </ul>
                    </div>
                    <div class="footer-widget">
                        <h4>友情链接</h4>
                        <ul class="footer-links">
                            {friend_link_html}
                        </ul>
                    </div>
                    <div class="footer-widget">
                        <h4>联系我</h4>
                        <div class="contact-info">
                            <p><i class="fas fa-envelope"></i> {email}</p>
                            <p><i class="fab fa-qq"></i> QQ群: {qq_group}</p>
                            <div class="social-links">
                                {connect_link_html}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <div class="container">
                {footer_bottom_html}
            </div>
        </div>
        <div class="back-to-top">
            <i class="fas fa-arrow-up"></i>
        </div>
    </footer>
    """

if __name__ == "__main__":
    print(footer(
        left_title="于小丘Blog",
        left_description="为了尚未完成的未来",
        fast_link={'主页': "/", "归档": "/archives", "关于": "/about"},
        friend_link={'于小丘Blog': "https://www.yxqi.cn", "海枫授权系统": "https://auth.yxqi.cn"},
        connect={"Github": "https://github.com/Yuerchu"},
        email="admin@yuxiaoqiu.cn",
        qq_group='140438837',
        weibo='/',
        bilibili="https://space.bilibili.com/361858612",
        twitter="/",
        footer_bottom=['Copyright (C) 2018-至今 于小丘Yuerchu.', '悦ICP备2024000000号']
    ))