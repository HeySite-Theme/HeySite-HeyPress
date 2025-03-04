from typing import Optional

def header(
    title_left: str,
    title_right: str,
    menu: dict,
    active: Optional[str] = None
):
    nav_menu = ""
    for name, url in menu.items():
        if name == active:
            nav_menu += f'<li><a href="{url}" class="active">{name}</a></li>\n'
        else:
            nav_menu += f'<li><a href="{url}">{name}</a></li>\n'
    return f"""
    <header class="navbar">
        <div class="container">
            <div class="logo">
                <a href="index.html">
                    <span class="logo-text">{title_left}<span class="highlight">{title_right}</span></span>
                </a>
            </div>
            <nav class="nav-menu">
                <ul>{nav_menu}</ul>
            </nav>
            <div class="auth-buttons">
                <div class="search-icon" id="searchIcon">
                    <i class="fas fa-search"></i>
                </div>
                <button class="btn-login" id="loginBtn">登录</button>
                <button class="btn-register" id="registerBtn">注册</button>
            </div>
            <div class="nav-toggle">
                <i class="fas fa-bars"></i>
            </div>
        </div>
    </header>
    """

if __name__ == "__main__":
    print(header(
        title_left = "于小丘",
        title_right = "Blog",
        menu = {"首页": "/", "关于": "/about"}
    ))