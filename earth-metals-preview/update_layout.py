import re

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update Hero Section
    new_hero = """
    <section id="home" class="home_banner grouping dark-bg">
        <div class="custom_container">
            <div class="row">
                <div class="col-md-12 d-flex align-items-center">
                    <div class="head_CTA">
                        <h1 class="white mb-4 font_700 main_font">Beyond the Bid.</h1>
                        <h4 class="white font_700 mb-4" style="color: #FFCD05;">Africa's Trusted B2B Marketplace for Commercial Vehicles, Equipment & Parts.</h4>
                        <div>
                            <p class="mb-5 font_400 white" style="max-width: 600px; font-size: 1.1rem; line-height: 1.6;">Earth Metals connects verified sellers with qualified buyers across Southern Africa. Whether you are disposing of a fleet, sourcing work-ready machinery, or expanding your procurement reach, our platform delivers inspected assets, transparent auctions, and secure transactions, all in one place.</p>
                            
                            <div class="hero_cta_buttons">
                                <a class="prim_btn" href="#">Explore Auctions</a>
                                <a class="prim_btn outline" href="/site/register">Register to Bid</a>
                            </div>

                            <div class="trust-bar">
                                <div class="trust-item"><span class="iconify" data-icon="mdi:check-decagram"></span> Verified Sellers</div>
                                <div class="trust-item"><span class="iconify" data-icon="mdi:magnify-scan"></span> Inspected Assets</div>
                                <div class="trust-item"><span class="iconify" data-icon="mdi:gavel"></span> Transparent Bidding</div>
                                <div class="trust-item"><span class="iconify" data-icon="mdi:shield-check"></span> Secure Transactions</div>
                                <div class="trust-item"><span class="iconify" data-icon="mdi:earth"></span> Serving Southern Africa</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""
    # Replace the old hero section
    hero_pattern = re.compile(r'<section id="home".*?</section>', re.DOTALL)
    html = re.sub(hero_pattern, new_hero, html, count=1)

    # 2. Add Poppins Font to Head
    poppins_font = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">\n'
    if 'family=Poppins' not in html:
        html = html.replace('<!-- Google Font -->', '<!-- Google Font -->\n    ' + poppins_font)

    # 3. Update the Asset Badges in the Services Section
    badge_replacements = html.replace('badge bg-secondary', 'asset-badge')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(badge_replacements)

if __name__ == "__main__":
    main()
