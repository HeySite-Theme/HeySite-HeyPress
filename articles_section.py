def articles_section(
    group_id: str,
    group_name: str,
    group_icon: str,
    group_content: str
):
    """
    卡片组布局
    """
    return f"""
    <section class="articles-section" id="{group_id}">
        <h2 class="section-title"><i class="{group_icon}"></i> {group_name}</h2>
        
        <div class="articles-container">
            {group_content}
            
            <div class="load-more-container">
                <button id="load-more" class="btn primary">加载更多</button>
            </div>
        </div>
    </section>
    """

def create_card(
    img_url: str,
    img_alt: str,
    badge: str,
    badge_class: str,
    article_title: str,
    meta_article_date: str,
    meta_article_eye: str,
    meta_article_comment: str,
    article_excerpt: str,
    read_more_url: str
):
    """
    创建卡片
    ~~~
    :param img_url: 卡片顶部的图片URL
    :param img_alt: 卡片顶部图片的alt属性，在无网络时显示，也能带来更好的SEO
    :param badge: 卡片右上角的徽章，用于显示 置顶或者文章分类
    :param badge_class: 徽章的属性
    :param article_title: 文章的标题
    :param meta_article_date: 文章的发布日期
    :param meta_article_eye: 文章的阅读量
    :param meta_article_comment: 文章的评论数
    :param article_excerpt: 文章内容的第一段，超出长度会自动压缩
    :param read_more_url: 文章的URL

    :return: HTML
    """
    return f"""
    <article class="article-card">
        <div class="article-image">
            <img src="{img_url}" alt="{img_alt}">
            <div class="{badge_class}">{badge}</div>
        </div>
        <div class="article-content">
            <h3 class="article-title">{article_title}</h3>
            <div class="article-meta">
                <span><i class="far fa-calendar"></i> {meta_article_date}</span>
                <span><i class="far fa-eye"></i> {meta_article_eye}</span>
                <span><i class="far fa-comment"></i> {meta_article_comment}</span>
            </div>
            <p class="article-excerpt">{article_excerpt}</p>
            <a href="{read_more_url}" class="read-more">阅读更多 <i class="fas fa-arrow-right"></i></a>
        </div>
    </article>
    """