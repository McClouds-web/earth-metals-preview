import re
import os

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add Head Meta Tags & Tracking Scripts
    head_additions = """
    <!-- Blueprint SEO & Tracking Scripts -->
    <meta name="description" content="Earth Metals is a trusted B2B online marketplace for commercial vehicles, plant equipment, and parts across Southern Africa. Buy and sell with confidence. Verified listings. Transparent auctions.">
    <meta property="og:title" content="Earth Metals: Trade Commercial Assets Across Africa">
    <meta property="og:description" content="Buy and sell inspected commercial vehicles, heavy equipment, and parts through a trusted B2B platform serving Southern Africa.">
    
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Organization",
      "name": "Earth Metals",
      "url": "https://www.earth-metals.com",
      "contactPoint": [
        { "@type": "ContactPoint", "telephone": "+27-84-062-8040", "contactType": "customer service", "contactOption": "TollFree", "areaServed": "ZA" },
        { "@type": "ContactPoint", "telephone": "+263-242-870-965", "contactType": "customer service", "areaServed": "ZW" }
      ]
    }
    </script>

    <!-- GA4 Placeholder -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-XXXXXXXXXX');
    </script>
    <!-- Meta Pixel Placeholder -->
    <script>
      !function(f,b,e,v,n,t,s)
      {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
      n.callMethod.apply(n,arguments):n.queue.push(arguments)};
      if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
      n.queue=[];t=b.createElement(e);t.async=!0;
      t.src=v;s=b.getElementsByTagName(e)[0];
      s.parentNode.insertBefore(t,s)}(window, document,'script',
      'https://connect.facebook.net/en_US/fbevents.js');
      fbq('init', 'XXXXXXXXXXXXXXX');
      fbq('track', 'PageView');
    </script>
    <!-- End Blueprint SEO & Tracking Scripts -->
"""
    if "Blueprint SEO" not in html:
        html = html.replace('</head>', head_additions + '\n</head>')

    # 2. Add New Sections from Blueprint
    new_sections = """

    <!-- BLUEPRINT NEW SECTIONS START -->
    <!-- SEC 2: PLATFORM INTRO -->
    <section class="pad_top_100 grouping">
        <div class="pd_bottom_60">
            <div class="custom_container">
                <div class="row">
                    <div class="col-sm-12 col-md-6">
                        <h2 class="sub_head_title main_font font_700"><span class="underlined">One</span> Platform. Every Asset. Across the Region.</h2>
                    </div>
                    <div class="col-sm-12 col-md-6">
                        <p>Earth Metals simplifies the buying and selling of commercial vehicles, plant equipment, and parts by replacing fragmented, offline trading with a structured, digital marketplace built for business.</p>
                        <p>Our platform brings together fleet owners, dealers, logistics providers, construction companies, mining operators, and agricultural businesses in a single, trusted environment. Every listing is verified. Every auction is transparent. Every transaction is supported from listing to handover.</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="pd_bottom_60">
            <div class="custom_container">
                <div class="row">
                    <div class="col-md-3 col-sm-6 mb-sm-4">
                        <div class="mit_border" style="height: 100%;">
                            <div class="d-flex justify-content-center flex-column">
                                <h3 class="font_25_30">Verified Listings</h3>
                                <p>Every asset is inspected and verified before listing. Buyers know exactly what they are acquiring.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3 col-sm-6 mb-sm-4">
                        <div class="mit_border" style="height: 100%;">
                            <div class="d-flex justify-content-center flex-column">
                                <h3 class="font_25_30">Transparent Bidding</h3>
                                <p>Real-time, competitive auctions with full price visibility. No hidden costs, no surprises.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3 col-sm-6 mb-sm-4">
                        <div class="mit_border" style="height: 100%;">
                            <div class="d-flex justify-content-center flex-column">
                                <h3 class="font_25_30">Secure Transactions</h3>
                                <p>Structured payment processes and documented handovers protect both buyer and seller at every stage.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3 col-sm-6 mb-sm-4">
                        <div class="mit_border" style="height: 100%;">
                            <div class="d-flex justify-content-center flex-column">
                                <h3 class="font_25_30">Regional Reach</h3>
                                <p>Access buyers and sellers across Southern Africa from a single platform. No borders, no barriers.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SEC 3: ABOUT US ADDITION -->
    <section class="pad_top_100 pd_bottom_60 px-0 grouping light-bg">
        <div class="custom_container">
            <div class="row">
                <div class="col-lg-6 col-md-5 padding_right_80">
                    <div class="about_img d-flex align-items-center justify-content-center" style="background: #eef; height: 100%; min-height: 300px; border-radius: 8px;">
                        <!-- Visual Guidance: confident industrial image -->
                        <span style="color:#888; text-align:center;">[Industrial Image Placeholder: Mining Hauler / Fleet Row]</span>
                    </div>
                </div>
                <div class="col-lg-6 col-md-7 d-flex align-items-center">
                    <div>
                        <h2 class="sub_head_title mb-4 main_font font_700"><span class="underlined">Built</span> for the Way Africa Does Business</h2>
                        <h5 class="mb-4">Earth Metals was created to solve a problem that every fleet owner, procurement manager, and equipment dealer knows too well. The commercial asset market across Africa is fragmented, inefficient, and hard to navigate.</h5>
                        <p>Buying or selling a truck, excavator, or fleet of vehicles should not rely on informal contacts, manual paperwork, or guesswork around pricing. As industries across Southern Africa grow and asset movements increase, the need for a structured, digital alternative has never been greater.</p>
                        <blockquote style="border-left: 4px solid #41A648; padding-left: 15px; margin-top: 20px; font-style: italic;">
                            "We exist to make the trading of commercial assets across Africa more structured, transparent, and reliable, from first bid to final handover."
                        </blockquote>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SEC 4: SERVICES / AUCTION -->
    <section class="pad_top_100 grouping">
        <div class="pd_bottom_60">
            <div class="custom_container">
                <div class="row mb-5">
                    <div class="col-sm-12 text-center">
                        <h2 class="sub_head_title main_font font_700"><span class="underlined">Trade</span> with Confidence Across Every Asset Class</h2>
                        <p>From single-unit disposals to large fleet auctions, Earth Metals gives your business a structured route to market and a reliable source of work-ready assets.</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6 mb-4">
                        <div class="mit_border" style="height: 100%;">
                            <h3 class="font_25_30 mb-3">Sell Faster. Reach Further.</h3>
                            <p>Earth Metals connects you with a network of qualified buyers across Southern Africa. List your vehicles, equipment, or parts with full inspection documentation and let competitive bidding do the work.</p>
                            <ul style="list-style-type: disc; padding-left: 20px;" class="mb-4">
                                <li>Reach verified buyers across South Africa, Zimbabwe, and the wider region</li>
                                <li>Professional inspection and documentation support</li>
                                <li>Structured auction process with transparent pricing</li>
                                <li>Faster disposal cycles with reduced administrative burden</li>
                                <li>Suitable for single units, batches, and complete fleet disposals</li>
                            </ul>
                            <a class="prim_btn" href="#">List Your Assets →</a>
                        </div>
                    </div>
                    <div class="col-md-6 mb-4">
                        <div class="mit_border" style="height: 100%;">
                            <h3 class="font_25_30 mb-3">Source Smarter. Buy with Certainty.</h3>
                            <p>Every asset listed on Earth Metals has been inspected, documented, and verified. Bid with confidence knowing exactly what you are acquiring. No guesswork, no hidden conditions.</p>
                            <ul style="list-style-type: disc; padding-left: 20px;" class="mb-4">
                                <li>Access inspected commercial vehicles, heavy equipment, and parts</li>
                                <li>Transparent bidding with real-time visibility</li>
                                <li>Secure payment and handover processes</li>
                                <li>Source stock across South Africa, Zimbabwe, and beyond</li>
                                <li>Suitable for procurement teams, fleet managers, and dealers</li>
                            </ul>
                            <a class="prim_btn" href="#">Explore Current Listings →</a>
                        </div>
                    </div>
                </div>
                
                <!-- Asset Categories -->
                <div class="row mt-4">
                    <div class="col-sm-12 text-center mb-4">
                        <h4 class="font_25_30">Asset Categories Available</h4>
                    </div>
                    <div class="col-sm-12 d-flex flex-wrap justify-content-center gap-2">
                        <span class="badge bg-secondary p-2 mb-2">Heavy Trucks & Haulage Vehicles</span>
                        <span class="badge bg-secondary p-2 mb-2">Trailers & Semi-Trailers</span>
                        <span class="badge bg-secondary p-2 mb-2">Construction & Earthmoving Equipment</span>
                        <span class="badge bg-secondary p-2 mb-2">Mining Machinery & Haul Trucks</span>
                        <span class="badge bg-secondary p-2 mb-2">Agricultural Equipment & Tractors</span>
                        <span class="badge bg-secondary p-2 mb-2">Buses & Passenger Vehicles</span>
                        <span class="badge bg-secondary p-2 mb-2">Light Commercial Vehicles</span>
                        <span class="badge bg-secondary p-2 mb-2">Plant & Industrial Equipment</span>
                        <span class="badge bg-secondary p-2 mb-2">Spare Parts & Components</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SEC 5: INDUSTRIES SERVED -->
    <section class="pad_top_100 pd_bottom_60 px-0 grouping light-bg">
        <div class="custom_container">
            <div class="row mb-5">
                <div class="col-sm-12 text-center">
                    <h2 class="sub_head_title main_font font_700"><span class="underlined">The</span> Industries We Serve</h2>
                    <p style="max-width: 800px; margin: 0 auto;">Earth Metals is built for businesses that depend on commercial vehicles and heavy equipment to operate, grow, and deliver results. We understand the procurement and disposal pressures unique to each sector.</p>
                </div>
            </div>
            <div class="row">
                <div class="col-md-4 mb-4">
                    <div class="mit_border" style="height: 100%;">
                        <div class="d-flex justify-content-center flex-column">
                            <h3 class="font_25_30">Mining & Resources</h3>
                            <p>Haul trucks, excavators, and support vehicles for surface and underground operations. Source or dispose of high-value mining assets with full documentation.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4 mb-4">
                    <div class="mit_border" style="height: 100%;">
                        <div class="d-flex justify-content-center flex-column">
                            <h3 class="font_25_30">Construction</h3>
                            <p>Earthmoving equipment, graders, loaders, and plant machinery for infrastructure and commercial construction projects across the region.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4 mb-4">
                    <div class="mit_border" style="height: 100%;">
                        <div class="d-flex justify-content-center flex-column">
                            <h3 class="font_25_30">Logistics & Transport</h3>
                            <p>Trucks, trailers, and refrigerated vehicles for cross-border logistics and last-mile delivery operators managing large and growing fleets.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4 mb-4">
                    <div class="mit_border" style="height: 100%;">
                        <div class="d-flex justify-content-center flex-column">
                            <h3 class="font_25_30">Agriculture</h3>
                            <p>Tractors, combine harvesters, irrigation equipment, and transport vehicles for commercial farming and agribusiness operations.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4 mb-4">
                    <div class="mit_border" style="height: 100%;">
                        <div class="d-flex justify-content-center flex-column">
                            <h3 class="font_25_30">Fleet Dealers & Resellers</h3>
                            <p>Dealers and resellers seeking a direct, efficient channel to source stock and dispose of inventory through competitive, transparent auctions.</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4 mb-4">
                    <div class="mit_border" style="height: 100%;">
                        <div class="d-flex justify-content-center flex-column">
                            <h3 class="font_25_30">Financial Institutions</h3>
                            <p>Banks, leasing companies, and asset financiers requiring structured, transparent disposal of repossessed or end-of-lease commercial assets.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SEC 6: WHY CHOOSE EARTH METALS -->
    <section class="pad_top_100 pad_bottom_100 px-0 grouping">
        <div class="custom_container">
            <div class="row">
                <div class="col-md-5 mb-4 d-flex align-items-center">
                    <div>
                        <h2 class="sub_head_title main_font font_700"><span class="underlined">Why</span> Businesses Choose Earth Metals</h2>
                        <p class="mb-4">In a market where commercial asset transactions have traditionally been slow, informal, and unpredictable, Earth Metals brings structure, speed, and confidence to every transaction.</p>
                    </div>
                </div>
                <div class="col-md-7">
                    <div class="mb-4">
                        <h4 class="font_700" style="color:#41A648;">01 Verified, Inspected Assets</h4>
                        <p>Every vehicle and piece of equipment listed on Earth Metals is professionally inspected before going to auction. Buyers receive accurate condition reports, service history documentation, and transparent asset records, removing the risk and uncertainty of uninspected purchases.</p>
                    </div>
                    <div class="mb-4">
                        <h4 class="font_700" style="color:#41A648;">02 Qualified, Verified Participants Only</h4>
                        <p>Earth Metals is a closed, business-to-business marketplace. Buyers and sellers are vetted before participation, ensuring every interaction is with a legitimate, capable counterparty. This eliminates wasted time, unqualified enquiries, and fraudulent activity.</p>
                    </div>
                    <div class="mb-4">
                        <h4 class="font_700" style="color:#41A648;">03 Transparent Pricing, No Surprises</h4>
                        <p>Real-time competitive bidding means prices are determined by the market, not by negotiation or guesswork. Both buyer and seller have full visibility throughout the process, with no hidden fees or last-minute changes.</p>
                    </div>
                    <div class="mb-4">
                        <h4 class="font_700" style="color:#41A648;">04 Structured, End-to-End Process</h4>
                        <p>From listing to payment and handover, every transaction on Earth Metals follows a clearly defined workflow. This reduces delays, prevents disputes, and ensures both parties have a consistent, reliable experience regardless of asset type or transaction size.</p>
                    </div>
                    <div class="mb-4">
                        <h4 class="font_700" style="color:#41A648;">05 Pan-African Reach from Day One</h4>
                        <p>With offices in Johannesburg and Harare and operations serving the wider Southern African region, Earth Metals provides access to a cross-border buyer and seller network that no single local marketplace can match.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- SEC 7: HOW IT WORKS -->
    <section class="pad_top_100 pd_bottom_60 px-0 grouping light-bg">
        <div class="custom_container">
            <div class="row mb-5 text-center">
                <div class="col-sm-12">
                    <h2 class="sub_head_title main_font font_700"><span class="underlined">Simple.</span> Structured. Secure.</h2>
                    <p>The Earth Metals process is designed to remove friction from buying and selling high-value commercial assets. Here is how it works:</p>
                </div>
            </div>

            <!-- Sellers Process -->
            <div class="row mb-5">
                <h3 class="mb-4 text-center w-100">Process Steps: For Sellers</h3>
                <div class="col-md-3 mb-4 text-center">
                    <div class="p-3" style="border-top: 4px solid #41A648;">
                        <span class="d-block mb-2" style="color:#888; font-weight:700;">STEP 1</span>
                        <h4 class="font_25_30" style="font-size:1.1rem;">Register & Verify</h4>
                        <p class="font_14" style="font-size:0.9rem;">Create your business account and complete verification.</p>
                    </div>
                </div>
                <div class="col-md-3 mb-4 text-center">
                    <div class="p-3" style="border-top: 4px solid #41A648;">
                        <span class="d-block mb-2" style="color:#888; font-weight:700;">STEP 2</span>
                        <h4 class="font_25_30" style="font-size:1.1rem;">List Your Asset</h4>
                        <p class="font_14" style="font-size:0.9rem;">Submit your asset for listing with photos, documentation, and inspection.</p>
                    </div>
                </div>
                <div class="col-md-3 mb-4 text-center">
                    <div class="p-3" style="border-top: 4px solid #41A648;">
                        <span class="d-block mb-2" style="color:#888; font-weight:700;">STEP 3</span>
                        <h4 class="font_25_30" style="font-size:1.1rem;">Auction Goes Live</h4>
                        <p class="font_14" style="font-size:0.9rem;">Qualified buyers bid in real time. You set the reserve. We manage the process.</p>
                    </div>
                </div>
                <div class="col-md-3 mb-4 text-center">
                    <div class="p-3" style="border-top: 4px solid #41A648;">
                        <span class="d-block mb-2" style="color:#888; font-weight:700;">STEP 4</span>
                        <h4 class="font_25_30" style="font-size:1.1rem;">Receive Payment & Handover</h4>
                        <p class="font_14" style="font-size:0.9rem;">Secure payment is confirmed before handover. Full documentation is provided.</p>
                    </div>
                </div>
            </div>

            <!-- Buyers Process -->
            <div class="row">
                <h3 class="mb-4 text-center w-100">Process Steps: For Buyers</h3>
                <div class="col-md-3 mb-4 text-center">
                    <div class="p-3" style="border-top: 4px solid #FFCD05;">
                        <span class="d-block mb-2" style="color:#888; font-weight:700;">STEP 1</span>
                        <h4 class="font_25_30" style="font-size:1.1rem;">Register & Verify</h4>
                        <p class="font_14" style="font-size:0.9rem;">Create your buyer account and complete business verification.</p>
                    </div>
                </div>
                <div class="col-md-3 mb-4 text-center">
                    <div class="p-3" style="border-top: 4px solid #FFCD05;">
                        <span class="d-block mb-2" style="color:#888; font-weight:700;">STEP 2</span>
                        <h4 class="font_25_30" style="font-size:1.1rem;">Browse & Review</h4>
                        <p class="font_14" style="font-size:0.9rem;">Explore current listings with full inspection reports and asset documentation.</p>
                    </div>
                </div>
                <div class="col-md-3 mb-4 text-center">
                    <div class="p-3" style="border-top: 4px solid #FFCD05;">
                        <span class="d-block mb-2" style="color:#888; font-weight:700;">STEP 3</span>
                        <h4 class="font_25_30" style="font-size:1.1rem;">Bid in Real Time</h4>
                        <p class="font_14" style="font-size:0.9rem;">Place bids on the assets you want. Watch live bidding and set your maximum.</p>
                    </div>
                </div>
                <div class="col-md-3 mb-4 text-center">
                    <div class="p-3" style="border-top: 4px solid #FFCD05;">
                        <span class="d-block mb-2" style="color:#888; font-weight:700;">STEP 4</span>
                        <h4 class="font_25_30" style="font-size:1.1rem;">Pay & Take Delivery</h4>
                        <p class="font_14" style="font-size:0.9rem;">Complete payment securely and arrange delivery or collection across the region.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- BLUEPRINT NEW SECTIONS END -->

"""
    if "BLUEPRINT NEW SECTIONS START" not in html:
        # Insert them right before the contactus section id block
        html = html.replace('<section id="contactus"', new_sections + '\n<section id="contactus"')

    
    # Update Contact Info to match blueprint slightly (we keep the current form but add the addresses above it)
    contact_updates = """
                        <div class="mb-4 d-flex justify-content-between flex-wrap">
                            <div class="mb-3" style="min-width: 48%;">
                                <h5 class="font_700">South Africa</h5>
                                <p class="mb-0">155 West Street</p>
                                <p class="mb-0">Sandton, Johannesburg</p>
                                <p class="mb-0">+27 84 062 8040</p>
                                <p class="mb-0">info@earth-metals.com</p>
                            </div>
                            <div class="mb-3" style="min-width: 48%;">
                                <h5 class="font_700">Zimbabwe</h5>
                                <p class="mb-0">Block C, 1st Floor, Smatsatsa Office Park</p>
                                <p class="mb-0">Borrowdale, Harare</p>
                                <p class="mb-0">+263 242 870 965 / +263 77 5758 232</p>
                            </div>
                        </div>
"""
    if "South Africa" not in html and "Zimbabwe" not in html:
        # inject just before the form
        html = html.replace('<form class="form-vertical"', contact_updates + '\n                        <form class="form-vertical"')
        
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    main()
