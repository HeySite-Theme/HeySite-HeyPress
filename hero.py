def hero(
    title_left: str,
    title_right: str,
    description: str,
    pic_url: str
):
    return f"""
    <section class="hero">
        <div class="container">
            <div class="hero-content">
                <h1 class="animate-text">{title_left} <span class="highlight">{title_right}</span></h1>
                <p>{description}</p>
                <div class="hero-buttons">
                    <a href="#latest-posts" class="btn primary">最新文章</a>
                    <a href="/about" class="btn secondary">了解更多</a>
                </div>
            </div>
            <div class="banner-image">
                <img src="{pic_url}" alt="banner-image">
            </div>
        </div>
    </section>
    """