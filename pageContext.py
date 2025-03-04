from typing import Optional

def head(
    body: str, 
    add_head_html: Optional[dict] = ''):
    """
    页面创建器上下文管理。创建 HeySite 主题页面必须使用此方法创建。
    """
    return f"""
    <!DOCTYPE html>_
    <html lang="zh-CN">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HeyPress - 二次元博客</title>
        <link rel="stylesheet" href="/public/css/main.css">
        <link rel="stylesheet" href="/public/css/all.min.css">
        <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&display=swap" rel="stylesheet">
        {add_head_html}</head><body>{body}<script src="/public/js/gsap.min.js"></script><script src="/public/js/main.js"></script></body></html>"""

def main_page_content(
    articles_sections: str
):
    return f"""
    <main class="main-content">
        <div class="container">
            <div class="content-grid">
                {articles_sections}
            </div>
        </div>
    </main>
    """

if __name__ == "__main__":
    from header import header
    from footer import footer
    print(head(body=header(
        title_left = "于小丘",
        title_right = "Blog",
        menu = {"首页": "/", "关于": "/about"}
    ) + footer(
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
    )))