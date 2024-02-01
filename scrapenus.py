import requests
from bs4 import BeautifulSoup
import json

# URLs of the pages to scrape
urls = [
    ["""<html style="height:100%"><head><meta content="NOINDEX, NOFOLLOW" name="ROBOTS"/><meta content="telephone=no" name="format-detection"/><meta content="initial-scale=1.0" name="viewport"/><meta content="IE=edge,chrome=1" http-equiv="X-UA-Compatible"/><script src="/_Incapsula_Resource?SWJIYLWA=719d34d31c8e3a6e6fffd425f7e032f3" type="text/javascript"></script></head><body style="margin:0px;height:100%"><iframe frameborder="0" height="100%" id="main-iframe" marginheight="0px" marginwidth="0px" src="/_Incapsula_Resource?SWUDNSAI=31&amp;xinfo=8-8882264-0%200NNN%20RT%281706810746585%2030%29%20q%280%20-1%20-1%20-1%29%20r%280%20-1%29%20B12%284%2c315%2c0%29%20U18&amp;incident_id=1559000650089863198-45118541352341576&amp;edet=12&amp;cinfo=04000000&amp;rpinfo=0&amp;cts=aO5bIGaj06i2n0Eh4ec%2fn4d39ceYZ98BZmNaIyvsdLCQabrBalcaxMTGs6SxE1AL&amp;mth=GET" width="100%">Request unsuccessful. Incapsula incident ID: 1559000650089863198-45118541352341576</iframe></body></html>""","Kent Ridge"],
    ["""<body itemtype="https://schema.org/WebPage" itemscope="itemscope" class="page-template-default page page-id-999 page-child parent-pageid-380 wp-custom-logo nus nus-astra ast-header-break-point ast-plain-container ast-no-sidebar astra-4.4.1 ast-header-custom-item-inside group-blog ast-single-post ast-inherit-site-logo-transparent wpb-js-composer js-comp-ver-7.0 vc_responsive elementor-default elementor-kit-5538 vsc-initialized" style="">

<div id="page" class="hfeed site">
	<a class="skip-link screen-reader-text" href="#content">Skip to content</a>

	
			<header class="site-header header-main-layout-1 ast-primary-menu-enabled ast-menu-toggle-icon ast-mobile-header-inline" id="masthead" itemtype="https://schema.org/WPHeader" itemscope="itemscope" itemid="#masthead">
			
<div class="main-header-bar-wrap">
	<div class="main-header-bar">
				<div class="ast-container">

			<div class="ast-flex main-header-container">
				
		<div class="site-branding">
			<div class="nus-site-logo-link">
				<a class="nus-site-img-link" href="http://www.nus.edu.sg" title="National University of Singapore">
					<img src="https://uci.nus.edu.sg/oca/wp-content/themes/nus-astra/assets/images/nus-logo.png" alt="NUS Logo">
				</a>
			</div>
			<div class="ast-site-identity hidden-sm hidden-xs" itemscope="itemscope" itemtype="https://schema.org/Organization">
				<span class="site-logo-img"><a href="https://uci.nus.edu.sg/oca/" class="custom-logo-link" rel="home"><img width="314" height="66" src="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2022/01/cropped-campuslife_logo.png" class="custom-logo" alt="Campus Services" decoding="async" srcset="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2022/01/cropped-campuslife_logo.png 314w, https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2022/01/cropped-campuslife_logo-300x63.png 300w" sizes="(max-width: 314px) 100vw, 314px"></a></span>			</div>
		</div><!-- .site-branding -->

		<div class="nus-quicklinks-container hidden-xs hidden-sm">
			<!-- QUICKLINKS -->
			<div class="nus-quicklinks">
				<ul id="menu-top-menu" class="box nav nav-pills menu"><li id="menu-item-1213" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1213"><a href="/about-us/" class="menu-link">About UCI</a></li>
<li id="menu-item-1214" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1214"><a href="http://news.nus.edu.sg/" class="menu-link">NUS News</a></li>
<li id="menu-item-1215" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1215"><a href="https://myportal.nus.edu.sg/studentportal/alerts/all/" class="menu-link">Student</a></li>
<li id="menu-item-1216" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1216"><a href="http://www.nus.edu.sg/staff" class="menu-link">Staff</a></li>
</ul>			</div>
			<!-- //QUICKLINKS -->
		</div>
				<div class="ast-mobile-menu-buttons">

			
					<div class="ast-button-wrap">
			<button type="button" class="menu-toggle main-header-menu-toggle  ast-mobile-menu-buttons-fill " aria-controls="primary-menu" aria-expanded="false" data-index="0">
				<span class="screen-reader-text">Main Menu</span>
				<span class="ast-icon icon-menu-bars"><span class="menu-toggle-icon"></span></span>							</button>
		</div>
			
			
		</div>
						</div><!-- Main Header Container -->
		</div><!-- ast-row -->
				<div class="nus-main-menu-container">
			<div class="ast-container">

				<div class="ast-main-header-bar-alignment"><div class="main-header-bar-navigation"><nav class="site-navigation ast-flex-grow-1 navigation-accessibility" id="primary-site-navigation" aria-label="Site Navigation" itemtype="https://schema.org/SiteNavigationElement" itemscope="itemscope"><div class="main-navigation"><ul id="primary-menu" class="main-header-menu ast-menu-shadow ast-nav-menu ast-flex ast-justify-content-flex-end  submenu-with-border" aria-expanded="false"><li id="menu-item-655" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-655"><a href="https://uci.nus.edu.sg/oca/" class="menu-link">Home</a></li>
<li id="menu-item-478" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-478"><a href="https://uci.nus.edu.sg/oca/about-us/about-oca/" class="menu-link">About Campus Services</a></li>
<li id="menu-item-6494" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-6494" aria-haspopup="true"><a href="#" class="menu-link">Mobility Services</a><button class="ast-menu-toggle" aria-expanded="false"><span class="screen-reader-text">Menu Toggle</span><span class="ast-icon icon-arrow"></span></button>
<ul class="sub-menu">
	<li id="menu-item-506" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-506"><a href="https://uci.nus.edu.sg/oca/mobilityservices/introduction/" class="menu-link">Introduction</a></li>
	<li id="menu-item-501" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-501"><a href="https://uci.nus.edu.sg/oca/mobilityservices/getting-to-nus/" class="menu-link">Getting to NUS</a></li>
	<li id="menu-item-500" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-500"><a href="https://uci.nus.edu.sg/oca/mobilityservices/getting-around-nus/" class="menu-link">Internal Shuttle Bus</a></li>
	<li id="menu-item-504" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-504"><a href="https://uci.nus.edu.sg/oca/mobilityservices/parking-information/" class="menu-link">Parking Information</a></li>
	<li id="menu-item-503" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-503"><a href="https://uci.nus.edu.sg/oca/mobilityservices/logistics-support-services/" class="menu-link">Logistics Support Services</a></li>
	<li id="menu-item-6540" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6540"><a href="https://uci.nus.edu.sg/oca/mobilityservices/sustainable-mobility/" class="menu-link">Sustainable Mobility</a></li>
</ul>
</li>
<li id="menu-item-510" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-510" aria-haspopup="true"><a href="#" class="menu-link">Retail &amp; Dining</a><button class="ast-menu-toggle" aria-expanded="false"><span class="screen-reader-text">Menu Toggle</span><span class="ast-icon icon-arrow"></span></button>
<ul class="sub-menu">
	<li id="menu-item-507" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-507"><a href="https://uci.nus.edu.sg/oca/retail-dining/introduction/" class="menu-link">Introduction</a></li>
	<li id="menu-item-493" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-493"><a href="https://uci.nus.edu.sg/oca/retail-dining/food-and-beverages/" class="menu-link">Food and Beverages</a></li>
	<li id="menu-item-498" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-498"><a href="https://uci.nus.edu.sg/oca/retail-dining/retail/" class="menu-link">Retail</a></li>
	<li id="menu-item-5801" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-5801"><a href="https://uci.nus.edu.sg/oca/faqs/retail-and-dining/rds-new-leasing-opportunities/" class="menu-link">Leasing opportunities</a></li>
	<li id="menu-item-4322" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4322"><a href="https://uci.nus.edu.sg/oca/campus-food-delivery/" class="menu-link">Campus Food Delivery</a></li>
	<li id="menu-item-3743" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3743"><a href="https://uci.nus.edu.sg/oca/retail-dining/well-certification/" class="menu-link">WELL Certification</a></li>
	<li id="menu-item-6524" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6524"><a href="https://uci.nus.edu.sg/oca/retail-dining/well-being-healthy-lifestyle/" class="menu-link">Well-Being &amp; Healthy Lifestyle</a></li>
</ul>
</li>
<li id="menu-item-511" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-511" aria-haspopup="true"><a href="#" class="menu-link">Latest News</a><button class="ast-menu-toggle" aria-expanded="false"><span class="screen-reader-text">Menu Toggle</span><span class="ast-icon icon-arrow"></span></button>
<ul class="sub-menu">
	<li id="menu-item-486" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-486"><a href="https://uci.nus.edu.sg/oca/latest-news/announcements/" class="menu-link">Announcements</a></li>
	<li id="menu-item-488" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-488"><a href="https://uci.nus.edu.sg/oca/latest-news/awards/" class="menu-link">Awards</a></li>
	<li id="menu-item-487" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-487"><a href="https://uci.nus.edu.sg/oca/latest-news/appreciations/" class="menu-link">Appreciations</a></li>
</ul>
</li>
<li id="menu-item-512" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-512" aria-haspopup="true"><a href="#" class="menu-link">FAQs</a><button class="ast-menu-toggle" aria-expanded="false"><span class="screen-reader-text">Menu Toggle</span><span class="ast-icon icon-arrow"></span></button>
<ul class="sub-menu">
	<li id="menu-item-483" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-483"><a href="https://uci.nus.edu.sg/oca/faqs/transport/" class="menu-link">Mobility Services</a></li>
	<li id="menu-item-482" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-482"><a href="https://uci.nus.edu.sg/oca/faqs/retail-and-dining/" class="menu-link">Retail and Dining</a></li>
</ul>
</li>
<li id="menu-item-5531" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5531"><a href="https://uci.nus.edu.sg/contact-us/" class="menu-link">Contact Us</a></li>
</ul></div></nav></div></div>
				<!-- SEARCH BUTTON ICON - START -->
		        <div class="search-btn-box hidden-sm hidden-xs">
		            <a class="fa fa-search collapsed" data-toggle="collapse" data-target="#search-collapse" href="#">&nbsp;</a>
		        </div>
		        <!-- SEARCH BUTTON ICON - END -->
			</div>

		</div>
		</div> <!-- Main Header Bar -->
</div> <!-- Main Header Bar Wrap -->
	<!-- NUS SEARCH - START  (Must be Toggled from SEARCH BUTTON ICON)-->
	<div id="search-collapse" class="nus-search-box collapse">
		<div class="ast-container">
			<div class="search">
				<form action="https://uci.nus.edu.sg/oca" method="get" class="form-inline form-search" title="Type and press Enter to search." role="search">
					<div class="icon faicon fa-search fl-search-input"> </div>
					<input name="s" id="mod-search-searchword" class="form-control input-lg" type="text" placeholder="Search..." value="Search" onfocus="if (this.value == 'Search') { this.value = ''; }" onblur="if (this.value == '') this.value='Search';">
					<input type="hidden" name="domains" value="http://www.nus.edu.sg/registrar/">
					<input type="hidden" name="sitesearch" value="http://www.nus.edu.sg/registrar/">
				</form>
			</div>
		</div>
	</div>
	<!-- NUS SEARCH - ENDS -->
			</header><!-- #masthead -->
		
	
	
	<div id="content" class="site-content">

		<div class="ast-container">

		

	<div id="primary" class="content-area primary">

		
					<main id="main" class="site-main">
				<article class="post-999 page type-page status-publish ast-article-single" id="post-999" itemtype="https://schema.org/CreativeWork" itemscope="itemscope">
	
	
	<header class="entry-header ast-no-thumbnail ast-no-title ast-header-without-markup">
			</header> <!-- .entry-header -->


<div class="entry-content clear nus_vc_has_fullwidth" itemprop="text">

	
	<section class="wpb-content-wrapper"><div data-vc-full-width="true" data-vc-full-width-init="true" data-vc-stretch-content="true" class="vc_row wpb_row vc_row-fluid nus-blue-header vc_row-no-padding" style="position: relative; left: -20px; box-sizing: border-box; width: 390px; max-width: 390px;"><div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element ">
		<div class="wpb_wrapper">
			<h1>Food &amp; Beverages</h1>

		</div>
	</div>
</div></div></div></div><div class="vc_row-full-width vc_clearfix"></div><div class="vc_row wpb_row vc_row-fluid"><div class="wpb_column vc_column_container vc_col-sm-8"><div class="vc_column-inner"><div class="wpb_wrapper"><div class="vc_row wpb_row vc_inner vc_row-fluid vc_custom_1526629606410 vc_row-o-content-middle vc_row-flex"><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper"><div class="vc_btn3-container vc_btn3-inline"><a style="background-color:#ef7c00; color:#ffffff;" class="vc_general vc_btn3 vc_btn3-size-md vc_btn3-shape-square vc_btn3-style-custom" href="/oca/retail-dining/food-and-beverages/" title="">Kent Ridge</a></div></div></div></div><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper"><div class="vc_btn3-container vc_btn3-inline"><a style="background-color:#ef7c00; color:#ffffff;" class="vc_general vc_btn3 vc_btn3-size-md vc_btn3-shape-square vc_btn3-style-custom" href="/oca/retail-dining/food-and-beverages-bukit-timah/" title="">Bukit Timah</a></div></div></div></div><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper"><div class="vc_btn3-container vc_btn3-inline"><a style="background-color:#ef7c00; color:#ffffff;" class="vc_general vc_btn3 vc_btn3-size-md vc_btn3-shape-square vc_btn3-style-custom" href="/oca/retail-dining/food-and-beverage-utown/" title="">University Town</a></div></div></div></div></div>
<div class="vc_grid-container-wrapper vc_clearfix vc_grid-animation-fadeIn">
	<div class="vc_grid-container vc_clearfix wpb_content_element vc_basic_grid vc_custom_1562657159423" data-initial-loading-animation="fadeIn" data-vc-grid-settings="{&quot;page_id&quot;:999,&quot;style&quot;:&quot;pagination&quot;,&quot;action&quot;:&quot;vc_get_vc_grid_data&quot;,&quot;shortcode_id&quot;:&quot;1562657152705-378ccdb24cbecbe51e8748012e6e328a-10&quot;,&quot;items_per_page&quot;:&quot;10&quot;,&quot;auto_play&quot;:false,&quot;gap&quot;:30,&quot;speed&quot;:-1000,&quot;loop&quot;:&quot;&quot;,&quot;animation_in&quot;:&quot;&quot;,&quot;animation_out&quot;:&quot;&quot;,&quot;arrows_design&quot;:&quot;none&quot;,&quot;arrows_color&quot;:&quot;blue&quot;,&quot;arrows_position&quot;:&quot;inside&quot;,&quot;paging_design&quot;:&quot;pagination_rounded_square&quot;,&quot;paging_color&quot;:&quot;black&quot;,&quot;tag&quot;:&quot;vc_basic_grid&quot;}" data-vc-request="https://uci.nus.edu.sg/oca/wp-admin/admin-ajax.php" data-vc-post-id="999" data-vc-public-nonce="2da27ff555">
		
	<div class="vc_grid-loading" style="display: none;"></div><style data-type="vc_shortcodes-custom-css">.vc_custom_1534521947044{margin-top: -10px !important;}.vc_custom_1526612607150{background-color: rgba(255,255,255,0.2) !important;*background-color: rgb(255,255,255) !important;}.vc_custom_1534521762134{padding-left: 20px !important;}.vc_custom_1534520726761{padding-left: 20px !important;}</style><style>
img.wp-smiley,
img.emoji {
	display: inline !important;
	border: none !important;
	box-shadow: none !important;
	height: 1em !important;
	width: 1em !important;
	margin: 0 0.07em !important;
	vertical-align: -0.1em !important;
	background: none !important;
	padding: 0 !important;
}
</style>
	<ul class="vc_grid-filter vc_clearfix vc_grid-filter-default vc_grid-filter-size-md vc_grid-filter-center vc_grid-filter-color-grey" data-vc-grid-filter="post_tag"><li class="vc_active vc_grid-filter-item"><span data-vc-grid-filter-value="*">All</span></li><li class="vc_grid-filter-item"><span data-vc-grid-filter-value=".vc_grid-term-69">BTC-Western</span></li></ul><div class="vc_grid-filter-select vc_grid-filter-center vc_grid-filter-color-grey" data-vc-grid-filter-select="post_tag"><div class="vc_grid-styled-select"><select data-filter="post_tag"><option class="vc_active" value="*">All&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option><option value=".vc_grid-term-69">BTC-Western&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option></select><i class="vc_arrow-icon-navicon"></i>
		</div>
	</div><div class="vc_grid vc_row vc_grid-gutter-30px vc_pageable-wrapper vc_hook_hover owl-carousel vc_grid-owl-theme owl-loaded owl-drag" data-vc-pageable-content="true"><div class="owl-stage-outer owl-height" style="height: 1046.75px;"><div class="owl-stage" style="transform: translate3d(0px, 0px, 0px); transition: all 0s ease 0s; width: 330px;"><div class="owl-item active" style="width: 320px; margin-right: 10px;"><div class="vc_pageable-slide-wrapper"><div class="vc_grid-item vc_clearfix vc_col-sm-12 vc_grid-item-zone-c-right vc_grid-term-69 vc_visible-item fadeIn animated"><div class="vc_grid-item-mini vc_clearfix "><div class="vc_gitem-animated-block  vc_gitem-animate vc_gitem-animate-fadeIn" data-vc-animation="fadeIn"><div class="vc_gitem-zone vc_gitem-zone-a" style="height: 300px;background-image: url('https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2018/05/Reedz-BTC-1024x684.jpg') !important;"><img src="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2018/05/Reedz-BTC-1024x684.jpg" class="vc_gitem-zone-img" alt="(PENDING HALAL CERT)
Location: The Thinking Corner @ BTC Li Ka Shing Building
Seating Capacity: 20
Term Time &amp; Vacation Operating Hours:
Mon-Fri, 8.00am-5.00pm
Sat/Sun/PH closed
(Closed on 29-30 Dec 2022)"><div class="vc_gitem-zone-mini"></div></div><div class="vc_gitem-zone vc_gitem-zone-b vc_custom_1526612607150 vc-gitem-zone-height-mode-auto"><div class="vc_gitem-zone-mini"></div></div></div><div class="vc_gitem-zone vc_gitem-zone-c vc_custom_1534521947044"><div class="vc_gitem-zone-mini"><div class="vc_gitem_row vc_row vc_gitem-row-position-top"><div class="vc_col-sm-12 vc_gitem-col vc_gitem-col-align-"><div class="vc_custom_heading heading-orange vc_custom_1534521762134 vc_gitem-post-data vc_gitem-post-data-source-post_title"><h3 style="text-align: left">Reedz Cafe</h3></div><div class="vc_custom_heading vc_custom_1534520726761 vc_gitem-post-data vc_gitem-post-data-source-post_excerpt"><p style="text-align: left"></p><p>(PENDING HALAL CERT)<br>
Location: The Thinking Corner @ BTC Li Ka Shing Building<br>
Seating Capacity: 20<br>
Term Time &amp; Vacation Operating Hours:<br>
Mon-Fri, 8.00am-5.00pm<br>
Sat/Sun/PH closed<br>
(Closed on 29-30 Dec 2022)</p>
<p></p></div></div></div></div></div></div><div class="vc_clearfix"></div></div><div class="vc_grid-item vc_clearfix vc_col-sm-12 vc_grid-item-zone-c-right vc_visible-item fadeIn animated"><div class="vc_grid-item-mini vc_clearfix "><div class="vc_gitem-animated-block  vc_gitem-animate vc_gitem-animate-fadeIn" data-vc-animation="fadeIn"><div class="vc_gitem-zone vc_gitem-zone-a" style="height: 300px;background-image: url('https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2018/05/BTC-1024x684.jpg') !important;"><img src="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2018/05/BTC-1024x684.jpg" class="vc_gitem-zone-img" alt="Location: BTC Block B
Seating Capacity: 330
Number of Stalls: 7
Term Time Operating Hours^:
Mon-Fri, 7.00am-8.00pm
Sat, 7.00am-4.00pm
Vacation Operating Hours^:
Mon-Fri, 7.30am-6.00pm
Sat, 7.30am-2.30pm
(Some stalls are closed on 29-30 Dec 2022)
^Stalls’ operating hours vary"><div class="vc_gitem-zone-mini"></div></div><div class="vc_gitem-zone vc_gitem-zone-b vc_custom_1526612607150 vc-gitem-zone-height-mode-auto"><div class="vc_gitem-zone-mini"></div></div></div><div class="vc_gitem-zone vc_gitem-zone-c vc_custom_1534521947044"><div class="vc_gitem-zone-mini"><div class="vc_gitem_row vc_row vc_gitem-row-position-top"><div class="vc_col-sm-12 vc_gitem-col vc_gitem-col-align-"><div class="vc_custom_heading heading-orange vc_custom_1534521762134 vc_gitem-post-data vc_gitem-post-data-source-post_title"><h3 style="text-align: left">The Summit</h3></div><div class="vc_custom_heading vc_custom_1534520726761 vc_gitem-post-data vc_gitem-post-data-source-post_excerpt"><p style="text-align: left"></p><p>Location: BTC Block B<br>
Seating Capacity: 330<br>
Number of Stalls: 7<br>
Term Time Operating Hours^:<br>
Mon-Fri, 7.00am-8.00pm<br>
Sat, 7.00am-4.00pm<br>
Vacation Operating Hours^:<br>
Mon-Fri, 7.30am-6.00pm<br>
Sat, 7.30am-2.30pm<br>
(Some stalls are closed on 29-30 Dec 2022)<br>
^Stalls’ operating hours vary</p>
<p></p></div></div></div></div></div></div><div class="vc_clearfix"></div></div></div></div></div></div><div class="vc_grid-owl-nav vc_grid-owl-nav-color-blue disabled"><div class="vc_grid-owl-prev none vc_grid-nav-prev-inside disabled"></div><div class="vc_grid-owl-next none vc_grid-nav-next-inside disabled"></div></div><div class="vc_grid-owl-dots vc_grid-pagination_rounded_square vc_grid-owl-dots-color-black disabled"><div class="vc_grid-owl-dot active"><span></span></div></div></div><div class="vc_grid-pagination"><ul class="vc_grid-pagination-list vc_grid-pagination_rounded_square vc_grid-pagination-color-black"><li class="vc_grid-page vc_grid-active"><a href="#" class="page-link">1</a></li></ul></div></div>
</div></div></div></div><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner vc_custom_1524725489751"><div class="wpb_wrapper"><div class="vc_wp_custommenu wpb_content_element nus-right-sidebar"><div class="widget widget_nav_menu"><nav class="menu-retail-dining-container" aria-label="Menu"><ul id="menu-retail-dining" class="menu"><li id="menu-item-399" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-399"><a href="https://uci.nus.edu.sg/oca/retail-dining/introduction/" class="menu-link">Introduction</a></li>
<li id="menu-item-398" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-398"><a href="https://uci.nus.edu.sg/oca/retail-dining/food-and-beverages/" class="menu-link">Food and Beverages</a></li>
<li id="menu-item-397" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-397"><a href="https://uci.nus.edu.sg/oca/retail-dining/retail/" class="menu-link">Retail</a></li>
<li id="menu-item-6307" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6307"><a href="https://uci.nus.edu.sg/oca/faqs/retail-and-dining/rds-new-leasing-opportunities/" class="menu-link">New Leasing opportunities</a></li>
<li id="menu-item-6489" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6489"><a href="https://uci.nus.edu.sg/oca/campus-food-delivery/" class="menu-link">Campus Food Delivery</a></li>
<li id="menu-item-6488" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6488"><a href="https://uci.nus.edu.sg/oca/retail-dining/well-certification/" class="menu-link">WELL Certification</a></li>
</ul></nav></div></div></div></div></div></div>
</section>
	
	
</div><!-- .entry-content .clear -->

	
	
</article><!-- #post-## -->

			</main><!-- #main -->
			
		
	</div><!-- #primary -->


	</div> <!-- ast-container -->
	</div><!-- #content -->

		<footer class="site-footer" id="colophon" itemtype="https://schema.org/WPFooter" itemscope="itemscope" itemid="#colophon">

			
			
<!-- NUS BREADCRUMBS - START -->
<div class="nus-breadcrumbs">
	<div class="ast-container">
		<ul><li class="item-home"><span class="icon faicon fa-map-marker"></span><a class="bread-link bread-home" href="https://uci.nus.edu.sg/oca" title="Homepage">Homepage</a></li><li class="item-parent item-parent-380"><a class="bread-parent bread-parent-380" href="https://uci.nus.edu.sg/oca/retail-dining/" title="Retail &amp; Dining">Retail &amp; Dining</a></li><li class="item-current item-999"><strong title="Food and Beverages – Bukit Timah"> Food and Beverages – Bukit Timah</strong></li></ul>	</div>
</div>
<!-- NUS BREADCRUMBS - END -->

<div class="footer-adv footer-adv-layout-4 nus-footer">
	<div class="footer-adv-overlay nus-footer-overlay">
		<div class="ast-container">
			<div class="ast-row navigator">
				<div class="ast-col-lg-12 ast-col-md-12 ast-col-sm-12 ast-col-xs-12 nus-footer-widget">

					<div class="ast-row">
						<div class="ast-col-lg-12 ast-col-md-12 ast-col-sm-12 ast-col-xs-12 footer-adv-widget footer-adv-widget-1 nus-footer-right-text">
							<div id="custom_html-2" class="widget_text widget widget_custom_html"><div class="textwidget custom-html-widget"><div class="nus-social-box">
    <div class="nus-module module">
        <div class="module-inner">
            <h3 class="title">Campus Life (Campus Services)</h3>
                <div class="module-ct">
                    <ul class="nus-contact-us">
                        <li>
							<span class="icon fa fa-location-arrow"></span>
							8 Kent Ridge Drive, #02-03<br>
							Singapore 119246
						</li>
                        <li>
							<span class="icon fa fa-phone"></span>
							+65 6601 7878 
						</li>
                        <li>
							<span class="icon fa fa-envelope"></span>
							<a href="mailto:csenquiry@nus.edu.sg">csenquiry@nus.edu.sg</a>
						</li>
                    </ul>
                </div>
            </div>
			<div class="nus-module module footnav-alt">
            <div class="module-inner">
                <div class="module-ct">
                    <div>
                     
                        <a target="_blank" href="https://www.instagram.com/nus_oca/" rel="noopener noreferrer"><img width="32" height="32" alt="instagram" src="/wp-content/themes/nus-astra/assets/images/instagram.png"></a>&nbsp;
                    </div>
                </div>
            </div>
        </div>
        </div>
    </div>
</div></div>						</div>
					</div>

				</div><!-- .nus-footer-widget -->
			</div><!-- .ast-row -->
		</div><!-- .ast-container -->
	</div><!-- .footer-adv-overlay-->
</div><!-- .ast-theme-footer .footer-adv-layout-4 -->

<div class="ast-small-footer footer-sml-layout-1">
	<div class="ast-footer-overlay">
		<div class="ast-container">
			<div class="ast-small-footer-wrap">
									<div class="ast-small-footer-section ast-small-footer-section-1">
						Copyright © 2024 <span class="ast-footer-site-title">Campus Services</span> | Powered by Websparks					</div>
				
				
			</div><!-- .ast-row .ast-small-footer-wrap -->
		</div><!-- .ast-container -->
	</div><!-- .ast-footer-overlay -->
</div><!-- .ast-small-footer-->

			
		</footer><!-- #colophon -->
			</div><!-- #page -->

		<script>
			window.RS_MODULES = window.RS_MODULES || {};
			window.RS_MODULES.modules = window.RS_MODULES.modules || {};
			window.RS_MODULES.waiting = window.RS_MODULES.waiting || [];
			window.RS_MODULES.defered = true;
			window.RS_MODULES.moduleWaiting = window.RS_MODULES.moduleWaiting || {};
			window.RS_MODULES.type = 'compiled';
		</script>
		            <div id="watsonconv-floating-box"></div>
        <link rel="stylesheet" id="lightbox2-css" href="https://uci.nus.edu.sg/oca/wp-content/plugins/js_composer/assets/lib/lightbox2/dist/css/lightbox.min.css?ver=7.0" media="all">
<link rel="stylesheet" id="vc_pageable_owl-carousel-css-css" href="https://uci.nus.edu.sg/oca/wp-content/plugins/js_composer/assets/lib/owl-carousel2-dist/assets/owl.min.css?ver=7.0" media="all">
<link rel="stylesheet" id="vc_animate-css-css" href="https://uci.nus.edu.sg/oca/wp-content/plugins/js_composer/assets/lib/bower/animate-css/animate.min.css?ver=7.0" media="all">
<link rel="stylesheet" id="rs-plugin-settings-css" href="https://uci.nus.edu.sg/oca/wp-content/plugins/revslider/public/assets/css/rs6.css?ver=6.6.16" media="all">
<style id="rs-plugin-settings-inline-css">
#rs-demo-id {}
</style>
<script id="astra-theme-js-js-extra">
var astra = {"break_point":"921","isRtl":"","is_scroll_to_id":"","is_scroll_to_top":"","is_header_footer_builder_active":""};
</script>
<script src="https://uci.nus.edu.sg/oca/wp-content/themes/astra/assets/js/minified/style.min.js?ver=4.4.1" id="astra-theme-js-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-content/plugins/revslider/public/assets/js/rbtools.min.js?ver=6.6.16" defer="" async="" id="tp-tools-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-content/plugins/revslider/public/assets/js/rs6.min.js?ver=6.6.16" defer="" async="" id="revmin-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-content/themes/nus-astra/assets/js/main.js?ver=20180228" id="nus-astra-navigation-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-content/plugins/js_composer/assets/js/dist/js_composer_front.min.js?ver=7.0" id="wpb_composer_front_js-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-content/plugins/js_composer/assets/lib/lightbox2/dist/js/lightbox.min.js?ver=7.0" id="lightbox2-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-content/plugins/js_composer/assets/lib/bower/twbs-pagination/jquery.twbsPagination.min.js?ver=7.0" id="twbs-pagination-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-content/plugins/js_composer/assets/lib/owl-carousel2-dist/owl.carousel.min.js?ver=7.0" id="vc_pageable_owl-carousel-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-content/plugins/js_composer/assets/lib/bower/imagesloaded/imagesloaded.pkgd.min.js?ver=7.0" id="vc_grid-js-imagesloaded-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-includes/js/underscore.min.js?ver=1.13.4" id="underscore-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-content/plugins/js_composer/assets/lib/vc_waypoints/vc-waypoints.min.js?ver=7.0" id="vc_waypoints-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-content/plugins/js_composer/assets/js/dist/vc_grid.min.js?ver=7.0" id="vc_grid-js"></script>
			<script>
			/(trident|msie)/i.test(navigator.userAgent)&&document.getElementById&&window.addEventListener&&window.addEventListener("hashchange",function(){var t,e=location.hash.substring(1);/^[A-z0-9_-]+$/.test(e)&&(t=document.getElementById(e))&&(/^(?:a|select|input|button|textarea)$/i.test(t.tagName)||(t.tabIndex=-1),t.focus())},!1);
			</script>
			<script></script>	

<div id="lightboxOverlay" tabindex="-1" class="lightboxOverlay" style="display: none;"></div><div id="lightbox" tabindex="-1" class="lightbox" style="display: none;"><div class="lb-outerContainer"><div class="lb-container"><img class="lb-image" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" alt=""><div class="lb-nav"><a class="lb-prev" aria-label="Previous image" href=""></a><a class="lb-next" aria-label="Next image" href=""></a></div><div class="lb-loader"><a class="lb-cancel"></a></div></div></div><div class="lb-dataContainer"><div class="lb-data"><div class="lb-details"><span class="lb-caption"></span><span class="lb-number"></span></div><div class="lb-closeContainer"><a class="lb-close"></a></div></div></div></div></body>""","Bukit Timah"],
    ["""<body itemtype="https://schema.org/WebPage" itemscope="itemscope" class="page-template-default page page-id-1010 page-child parent-pageid-380 wp-custom-logo nus nus-astra ast-header-break-point ast-plain-container ast-no-sidebar astra-4.4.1 ast-header-custom-item-inside group-blog ast-single-post ast-inherit-site-logo-transparent wpb-js-composer js-comp-ver-7.0 vc_responsive elementor-default elementor-kit-5538 vsc-initialized" style="">

<div id="page" class="hfeed site">
	<a class="skip-link screen-reader-text" href="#content">Skip to content</a>

	
			<header class="site-header header-main-layout-1 ast-primary-menu-enabled ast-menu-toggle-icon ast-mobile-header-inline" id="masthead" itemtype="https://schema.org/WPHeader" itemscope="itemscope" itemid="#masthead">
			
<div class="main-header-bar-wrap">
	<div class="main-header-bar">
				<div class="ast-container">

			<div class="ast-flex main-header-container">
				
		<div class="site-branding">
			<div class="nus-site-logo-link">
				<a class="nus-site-img-link" href="http://www.nus.edu.sg" title="National University of Singapore">
					<img src="https://uci.nus.edu.sg/oca/wp-content/themes/nus-astra/assets/images/nus-logo.png" alt="NUS Logo">
				</a>
			</div>
			<div class="ast-site-identity hidden-sm hidden-xs" itemscope="itemscope" itemtype="https://schema.org/Organization">
				<span class="site-logo-img"><a href="https://uci.nus.edu.sg/oca/" class="custom-logo-link" rel="home"><img width="314" height="66" src="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2022/01/cropped-campuslife_logo.png" class="custom-logo" alt="Campus Services" decoding="async" srcset="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2022/01/cropped-campuslife_logo.png 314w, https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2022/01/cropped-campuslife_logo-300x63.png 300w" sizes="(max-width: 314px) 100vw, 314px"></a></span>			</div>
		</div><!-- .site-branding -->

		<div class="nus-quicklinks-container hidden-xs hidden-sm">
			<!-- QUICKLINKS -->
			<div class="nus-quicklinks">
				<ul id="menu-top-menu" class="box nav nav-pills menu"><li id="menu-item-1213" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1213"><a href="/about-us/" class="menu-link">About UCI</a></li>
<li id="menu-item-1214" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1214"><a href="http://news.nus.edu.sg/" class="menu-link">NUS News</a></li>
<li id="menu-item-1215" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1215"><a href="https://myportal.nus.edu.sg/studentportal/alerts/all/" class="menu-link">Student</a></li>
<li id="menu-item-1216" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1216"><a href="http://www.nus.edu.sg/staff" class="menu-link">Staff</a></li>
</ul>			</div>
			<!-- //QUICKLINKS -->
		</div>
				<div class="ast-mobile-menu-buttons">

			
					<div class="ast-button-wrap">
			<button type="button" class="menu-toggle main-header-menu-toggle  ast-mobile-menu-buttons-fill " aria-controls="primary-menu" aria-expanded="false" data-index="0">
				<span class="screen-reader-text">Main Menu</span>
				<span class="ast-icon icon-menu-bars"><span class="menu-toggle-icon"></span></span>							</button>
		</div>
			
			
		</div>
						</div><!-- Main Header Container -->
		</div><!-- ast-row -->
				<div class="nus-main-menu-container">
			<div class="ast-container">

				<div class="ast-main-header-bar-alignment"><div class="main-header-bar-navigation"><nav class="site-navigation ast-flex-grow-1 navigation-accessibility" id="primary-site-navigation" aria-label="Site Navigation" itemtype="https://schema.org/SiteNavigationElement" itemscope="itemscope"><div class="main-navigation"><ul id="primary-menu" class="main-header-menu ast-menu-shadow ast-nav-menu ast-flex ast-justify-content-flex-end  submenu-with-border" aria-expanded="false"><li id="menu-item-655" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home menu-item-655"><a href="https://uci.nus.edu.sg/oca/" class="menu-link">Home</a></li>
<li id="menu-item-478" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-478"><a href="https://uci.nus.edu.sg/oca/about-us/about-oca/" class="menu-link">About Campus Services</a></li>
<li id="menu-item-6494" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-6494" aria-haspopup="true"><a href="#" class="menu-link">Mobility Services</a><button class="ast-menu-toggle" aria-expanded="false"><span class="screen-reader-text">Menu Toggle</span><span class="ast-icon icon-arrow"></span></button>
<ul class="sub-menu">
	<li id="menu-item-506" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-506"><a href="https://uci.nus.edu.sg/oca/mobilityservices/introduction/" class="menu-link">Introduction</a></li>
	<li id="menu-item-501" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-501"><a href="https://uci.nus.edu.sg/oca/mobilityservices/getting-to-nus/" class="menu-link">Getting to NUS</a></li>
	<li id="menu-item-500" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-500"><a href="https://uci.nus.edu.sg/oca/mobilityservices/getting-around-nus/" class="menu-link">Internal Shuttle Bus</a></li>
	<li id="menu-item-504" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-504"><a href="https://uci.nus.edu.sg/oca/mobilityservices/parking-information/" class="menu-link">Parking Information</a></li>
	<li id="menu-item-503" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-503"><a href="https://uci.nus.edu.sg/oca/mobilityservices/logistics-support-services/" class="menu-link">Logistics Support Services</a></li>
	<li id="menu-item-6540" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6540"><a href="https://uci.nus.edu.sg/oca/mobilityservices/sustainable-mobility/" class="menu-link">Sustainable Mobility</a></li>
</ul>
</li>
<li id="menu-item-510" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-510" aria-haspopup="true"><a href="#" class="menu-link">Retail &amp; Dining</a><button class="ast-menu-toggle" aria-expanded="false"><span class="screen-reader-text">Menu Toggle</span><span class="ast-icon icon-arrow"></span></button>
<ul class="sub-menu">
	<li id="menu-item-507" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-507"><a href="https://uci.nus.edu.sg/oca/retail-dining/introduction/" class="menu-link">Introduction</a></li>
	<li id="menu-item-493" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-493"><a href="https://uci.nus.edu.sg/oca/retail-dining/food-and-beverages/" class="menu-link">Food and Beverages</a></li>
	<li id="menu-item-498" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-498"><a href="https://uci.nus.edu.sg/oca/retail-dining/retail/" class="menu-link">Retail</a></li>
	<li id="menu-item-5801" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-5801"><a href="https://uci.nus.edu.sg/oca/faqs/retail-and-dining/rds-new-leasing-opportunities/" class="menu-link">Leasing opportunities</a></li>
	<li id="menu-item-4322" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4322"><a href="https://uci.nus.edu.sg/oca/campus-food-delivery/" class="menu-link">Campus Food Delivery</a></li>
	<li id="menu-item-3743" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-3743"><a href="https://uci.nus.edu.sg/oca/retail-dining/well-certification/" class="menu-link">WELL Certification</a></li>
	<li id="menu-item-6524" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6524"><a href="https://uci.nus.edu.sg/oca/retail-dining/well-being-healthy-lifestyle/" class="menu-link">Well-Being &amp; Healthy Lifestyle</a></li>
</ul>
</li>
<li id="menu-item-511" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-511" aria-haspopup="true"><a href="#" class="menu-link">Latest News</a><button class="ast-menu-toggle" aria-expanded="false"><span class="screen-reader-text">Menu Toggle</span><span class="ast-icon icon-arrow"></span></button>
<ul class="sub-menu">
	<li id="menu-item-486" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-486"><a href="https://uci.nus.edu.sg/oca/latest-news/announcements/" class="menu-link">Announcements</a></li>
	<li id="menu-item-488" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-488"><a href="https://uci.nus.edu.sg/oca/latest-news/awards/" class="menu-link">Awards</a></li>
	<li id="menu-item-487" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-487"><a href="https://uci.nus.edu.sg/oca/latest-news/appreciations/" class="menu-link">Appreciations</a></li>
</ul>
</li>
<li id="menu-item-512" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-512" aria-haspopup="true"><a href="#" class="menu-link">FAQs</a><button class="ast-menu-toggle" aria-expanded="false"><span class="screen-reader-text">Menu Toggle</span><span class="ast-icon icon-arrow"></span></button>
<ul class="sub-menu">
	<li id="menu-item-483" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-483"><a href="https://uci.nus.edu.sg/oca/faqs/transport/" class="menu-link">Mobility Services</a></li>
	<li id="menu-item-482" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-482"><a href="https://uci.nus.edu.sg/oca/faqs/retail-and-dining/" class="menu-link">Retail and Dining</a></li>
</ul>
</li>
<li id="menu-item-5531" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-5531"><a href="https://uci.nus.edu.sg/contact-us/" class="menu-link">Contact Us</a></li>
</ul></div></nav></div></div>
				<!-- SEARCH BUTTON ICON - START -->
		        <div class="search-btn-box hidden-sm hidden-xs">
		            <a class="fa fa-search collapsed" data-toggle="collapse" data-target="#search-collapse" href="#">&nbsp;</a>
		        </div>
		        <!-- SEARCH BUTTON ICON - END -->
			</div>

		</div>
		</div> <!-- Main Header Bar -->
</div> <!-- Main Header Bar Wrap -->
	<!-- NUS SEARCH - START  (Must be Toggled from SEARCH BUTTON ICON)-->
	<div id="search-collapse" class="nus-search-box collapse">
		<div class="ast-container">
			<div class="search">
				<form action="https://uci.nus.edu.sg/oca" method="get" class="form-inline form-search" title="Type and press Enter to search." role="search">
					<div class="icon faicon fa-search fl-search-input"> </div>
					<input name="s" id="mod-search-searchword" class="form-control input-lg" type="text" placeholder="Search..." value="Search" onfocus="if (this.value == 'Search') { this.value = ''; }" onblur="if (this.value == '') this.value='Search';">
					<input type="hidden" name="domains" value="http://www.nus.edu.sg/registrar/">
					<input type="hidden" name="sitesearch" value="http://www.nus.edu.sg/registrar/">
				</form>
			</div>
		</div>
	</div>
	<!-- NUS SEARCH - ENDS -->
			</header><!-- #masthead -->
		
	
	
	<div id="content" class="site-content">

		<div class="ast-container">

		

	<div id="primary" class="content-area primary">

		
					<main id="main" class="site-main">
				<article class="post-1010 page type-page status-publish ast-article-single" id="post-1010" itemtype="https://schema.org/CreativeWork" itemscope="itemscope">
	
	
	<header class="entry-header ast-no-thumbnail ast-no-title ast-header-without-markup">
			</header> <!-- .entry-header -->


<div class="entry-content clear nus_vc_has_fullwidth" itemprop="text">

	
	<section class="wpb-content-wrapper"><div data-vc-full-width="true" data-vc-full-width-init="true" data-vc-stretch-content="true" class="vc_row wpb_row vc_row-fluid nus-blue-header vc_row-no-padding" style="position: relative; left: -20px; box-sizing: border-box; width: 390px; max-width: 390px;"><div class="wpb_column vc_column_container vc_col-sm-12"><div class="vc_column-inner"><div class="wpb_wrapper">
	<div class="wpb_text_column wpb_content_element ">
		<div class="wpb_wrapper">
			<h1>Food &amp; Beverage</h1>

		</div>
	</div>
</div></div></div></div><div class="vc_row-full-width vc_clearfix"></div><div class="vc_row wpb_row vc_row-fluid"><div class="wpb_column vc_column_container vc_col-sm-8"><div class="vc_column-inner"><div class="wpb_wrapper"><div class="vc_row wpb_row vc_inner vc_row-fluid vc_custom_1526629224182"><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper"><div class="vc_btn3-container vc_btn3-inline"><a style="background-color:#ef7c00; color:#ffffff;" class="vc_general vc_btn3 vc_btn3-size-md vc_btn3-shape-square vc_btn3-style-custom" href="/oca/retail-dining/food-and-beverages/" title="">Kent Ridge</a></div></div></div></div><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper"><div class="vc_btn3-container vc_btn3-inline"><a style="background-color:#ef7c00; color:#ffffff;" class="vc_general vc_btn3 vc_btn3-size-md vc_btn3-shape-square vc_btn3-style-custom" href="/oca/retail-dining/food-and-beverages-bukit-timah/" title="">Bukit Timah</a></div></div></div></div><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner"><div class="wpb_wrapper"><div class="vc_btn3-container vc_btn3-inline"><a style="background-color:#ef7c00; color:#ffffff;" class="vc_general vc_btn3 vc_btn3-size-md vc_btn3-shape-square vc_btn3-style-custom" href="/oca/retail-dining/food-and-beverage-utown/" title="">University Town</a></div></div></div></div></div>
<div class="vc_grid-container-wrapper vc_clearfix vc_grid-animation-fadeIn">
	<div class="vc_grid-container vc_clearfix wpb_content_element vc_basic_grid vc_custom_1562656930767" data-initial-loading-animation="fadeIn" data-vc-grid-settings="{&quot;page_id&quot;:1010,&quot;style&quot;:&quot;all&quot;,&quot;action&quot;:&quot;vc_get_vc_grid_data&quot;,&quot;shortcode_id&quot;:&quot;1562656832367-b3426f5bbca26912816c15124a794d99-2&quot;,&quot;tag&quot;:&quot;vc_basic_grid&quot;}" data-vc-request="https://uci.nus.edu.sg/oca/wp-admin/admin-ajax.php" data-vc-post-id="1010" data-vc-public-nonce="2da27ff555">
		<style data-type="vc_shortcodes-custom-css">.vc_custom_1534521947044{margin-top: -10px !important;}.vc_custom_1526612607150{background-color: rgba(255,255,255,0.2) !important;*background-color: rgb(255,255,255) !important;}.vc_custom_1534521762134{padding-left: 20px !important;}.vc_custom_1534520726761{padding-left: 20px !important;}</style><ul class="vc_grid-filter vc_clearfix vc_grid-filter-default vc_grid-filter-size-md vc_grid-filter-center vc_grid-filter-color-grey" data-vc-grid-filter="post_tag"><li class="vc_active vc_grid-filter-item"><span data-vc-grid-filter-value="*">All</span></li><li class="vc_grid-filter-item"><span data-vc-grid-filter-value=".vc_grid-term-61">UT-Chinese</span></li><li class="vc_grid-filter-item"><span data-vc-grid-filter-value=".vc_grid-term-79">UT-Drink</span></li><li class="vc_grid-filter-item"><span data-vc-grid-filter-value=".vc_grid-term-77">UT-Halal</span></li><li class="vc_grid-filter-item"><span data-vc-grid-filter-value=".vc_grid-term-74">UT-Japanese</span></li><li class="vc_grid-filter-item"><span data-vc-grid-filter-value=".vc_grid-term-75">UT-Korean</span></li><li class="vc_grid-filter-item"><span data-vc-grid-filter-value=".vc_grid-term-76">UT-Western</span></li></ul><div class="vc_grid-filter-select vc_grid-filter-center vc_grid-filter-color-grey" data-vc-grid-filter-select="post_tag"><div class="vc_grid-styled-select"><select data-filter="post_tag"><option class="vc_active" value="*">All&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option><option value=".vc_grid-term-61">UT-Chinese&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option><option value=".vc_grid-term-79">UT-Drink&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option><option value=".vc_grid-term-77">UT-Halal&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option><option value=".vc_grid-term-74">UT-Japanese&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option><option value=".vc_grid-term-75">UT-Korean&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option><option value=".vc_grid-term-76">UT-Western&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</option></select><i class="vc_arrow-icon-navicon"></i>
		</div>
	</div><div class="vc_grid vc_row vc_grid-gutter-30px vc_pageable-wrapper vc_hook_hover" data-vc-pageable-content="true"><div class="vc_pageable-slide-wrapper vc_clearfix" data-vc-grid-content="true"><div class="vc_grid-item vc_clearfix vc_col-sm-12 vc_grid-item-zone-c-right vc_grid-term-77 vc_visible-item fadeIn animated"><div class="vc_grid-item-mini vc_clearfix "><div class="vc_gitem-animated-block  vc_gitem-animate vc_gitem-animate-fadeIn" data-vc-animation="fadeIn"><div class="vc_gitem-zone vc_gitem-zone-a" style="height: 300px;background-image: url('https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2022/08/Briyani-1024x660.jpg') !important;"><img src="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2022/08/Briyani-1024x660.jpg" class="vc_gitem-zone-img" alt="(MUSLIM OWNED)
Location: UTown Stephen Riady Centre (SRC)
Term Time &amp; Vacation Operating Hours:
Mon-Fri: 11.30am to 7.45pm
Sat: 11.30am to 5.30pm"><div class="vc_gitem-zone-mini"></div></div><div class="vc_gitem-zone vc_gitem-zone-b vc_custom_1526612607150 vc-gitem-zone-height-mode-auto"><div class="vc_gitem-zone-mini"></div></div></div><div class="vc_gitem-zone vc_gitem-zone-c vc_custom_1534521947044"><div class="vc_gitem-zone-mini"><div class="vc_gitem_row vc_row vc_gitem-row-position-top"><div class="vc_col-sm-12 vc_gitem-col vc_gitem-col-align-"><div class="vc_custom_heading heading-orange vc_custom_1534521762134 vc_gitem-post-data vc_gitem-post-data-source-post_title"><h3 style="text-align: left">Bismillah Biryani</h3></div><div class="vc_custom_heading vc_custom_1534520726761 vc_gitem-post-data vc_gitem-post-data-source-post_excerpt"><p style="text-align: left"></p><p>(MUSLIM OWNED)<br>
Location: UTown Stephen Riady Centre (SRC)<br>
Term Time &amp; Vacation Operating Hours:<br>
Mon-Fri: 11.30am to 7.45pm<br>
Sat: 11.30am to 5.30pm</p>
<p></p></div></div></div></div></div></div><div class="vc_clearfix"></div></div><div class="vc_grid-item vc_clearfix vc_col-sm-12 vc_grid-item-zone-c-right vc_grid-term-61 vc_visible-item fadeIn animated"><div class="vc_grid-item-mini vc_clearfix "><div class="vc_gitem-animated-block  vc_gitem-animate vc_gitem-animate-fadeIn" data-vc-animation="fadeIn"><div class="vc_gitem-zone vc_gitem-zone-a" style="height: 300px;background-image: url('https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2021/08/Chop-Cjop.jpg') !important;"><img src="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2021/08/Chop-Cjop.jpg" class="vc_gitem-zone-img" alt="Location: Town Plaza
Seating Capacity: 40
Term Time Operating Hours:
Mon-Sun, 11.00am-9.00pm (Last order 8.30pm)
Vacation Operating Hours:
Mon-Fri, 11.00am-8.00pm (Last order 7.30pm)
Sat-Sun: 11.00am-7.00pm
(Will be closed on 16-31 Dec 2022)
Contact: 63340201
Nearest Carpark: CREATE Tower"><div class="vc_gitem-zone-mini"></div></div><div class="vc_gitem-zone vc_gitem-zone-b vc_custom_1526612607150 vc-gitem-zone-height-mode-auto"><div class="vc_gitem-zone-mini"></div></div></div><div class="vc_gitem-zone vc_gitem-zone-c vc_custom_1534521947044"><div class="vc_gitem-zone-mini"><div class="vc_gitem_row vc_row vc_gitem-row-position-top"><div class="vc_col-sm-12 vc_gitem-col vc_gitem-col-align-"><div class="vc_custom_heading heading-orange vc_custom_1534521762134 vc_gitem-post-data vc_gitem-post-data-source-post_title"><h3 style="text-align: left">Chop Chop by PUTIEN</h3></div><div class="vc_custom_heading vc_custom_1534520726761 vc_gitem-post-data vc_gitem-post-data-source-post_excerpt"><p style="text-align: left"></p><p>Location: Town Plaza<br>
Seating Capacity: 40<br>
Term Time Operating Hours:<br>
Mon-Sun, 11.00am-9.00pm (Last order 8.30pm)<br>
Vacation Operating Hours:<br>
Mon-Fri, 11.00am-8.00pm (Last order 7.30pm)<br>
Sat-Sun: 11.00am-7.00pm<br>
(Will be closed on 16-31 Dec 2022)<br>
Contact: 63340201<br>
Nearest Carpark: CREATE Tower</p>
<p></p></div></div></div></div></div></div><div class="vc_clearfix"></div></div><div class="vc_grid-item vc_clearfix vc_col-sm-12 vc_grid-item-zone-c-right vc_visible-item fadeIn animated"><div class="vc_grid-item-mini vc_clearfix "><div class="vc_gitem-animated-block  vc_gitem-animate vc_gitem-animate-fadeIn" data-vc-animation="fadeIn"><div class="vc_gitem-zone vc_gitem-zone-a" style="height: 300px;background-image: url('https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2018/05/Fine-Food-1-1024x684.jpg') !important;"><img src="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2018/05/Fine-Food-1-1024x684.jpg" class="vc_gitem-zone-img" alt="(2 STALL PENDING HALAL CERT)
Location: Town Plaza
Seating Capacity: 410
Number of Stalls: 14
Term Time &amp; Vacation Operating Hours:
Mon-Sun, 8.00am-8.30pm"><div class="vc_gitem-zone-mini"></div></div><div class="vc_gitem-zone vc_gitem-zone-b vc_custom_1526612607150 vc-gitem-zone-height-mode-auto"><div class="vc_gitem-zone-mini"></div></div></div><div class="vc_gitem-zone vc_gitem-zone-c vc_custom_1534521947044"><div class="vc_gitem-zone-mini"><div class="vc_gitem_row vc_row vc_gitem-row-position-top"><div class="vc_col-sm-12 vc_gitem-col vc_gitem-col-align-"><div class="vc_custom_heading heading-orange vc_custom_1534521762134 vc_gitem-post-data vc_gitem-post-data-source-post_title"><h3 style="text-align: left">Fine Food</h3></div><div class="vc_custom_heading vc_custom_1534520726761 vc_gitem-post-data vc_gitem-post-data-source-post_excerpt"><p style="text-align: left"></p><p>(2 STALL PENDING HALAL CERT)<br>
Location: Town Plaza<br>
Seating Capacity: 410<br>
Number of Stalls: 14<br>
Term Time &amp; Vacation Operating Hours:<br>
Mon-Sun, 8.00am-8.30pm</p>
<p></p></div></div></div></div></div></div><div class="vc_clearfix"></div></div><div class="vc_grid-item vc_clearfix vc_col-sm-12 vc_grid-item-zone-c-right vc_grid-term-77 vc_visible-item fadeIn animated"><div class="vc_grid-item-mini vc_clearfix "><div class="vc_gitem-animated-block  vc_gitem-animate vc_gitem-animate-fadeIn" data-vc-animation="fadeIn"><div class="vc_gitem-zone vc_gitem-zone-a" style="height: 300px;background-image: url('https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2018/05/Flavours-Edited-1024x684.jpg') !important;"><img src="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2018/05/Flavours-Edited-1024x684.jpg" class="vc_gitem-zone-img" alt="(HALAL FOOD OPTIONS AVAILABLE)
Location: UTown Stephen Riady Centre
Seating Capacity: 700
Number of Stalls: 11
Term Time &amp; Vacation Operating Hours:
Mon-Sun: 7.30am to 8.30pm"><div class="vc_gitem-zone-mini"></div></div><div class="vc_gitem-zone vc_gitem-zone-b vc_custom_1526612607150 vc-gitem-zone-height-mode-auto"><div class="vc_gitem-zone-mini"></div></div></div><div class="vc_gitem-zone vc_gitem-zone-c vc_custom_1534521947044"><div class="vc_gitem-zone-mini"><div class="vc_gitem_row vc_row vc_gitem-row-position-top"><div class="vc_col-sm-12 vc_gitem-col vc_gitem-col-align-"><div class="vc_custom_heading heading-orange vc_custom_1534521762134 vc_gitem-post-data vc_gitem-post-data-source-post_title"><h3 style="text-align: left">Flavours @ UTown</h3></div><div class="vc_custom_heading vc_custom_1534520726761 vc_gitem-post-data vc_gitem-post-data-source-post_excerpt"><p style="text-align: left"></p><p>(HALAL FOOD OPTIONS AVAILABLE)<br>
Location: UTown Stephen Riady Centre<br>
Seating Capacity: 700<br>
Number of Stalls: 11<br>
Term Time &amp; Vacation Operating Hours:<br>
Mon-Sun: 7.30am to 8.30pm</p>
<p></p></div></div></div></div></div></div><div class="vc_clearfix"></div></div><div class="vc_grid-item vc_clearfix vc_col-sm-12 vc_grid-item-zone-c-right vc_grid-term-75 vc_visible-item fadeIn animated"><div class="vc_grid-item-mini vc_clearfix "><div class="vc_gitem-animated-block  vc_gitem-animate vc_gitem-animate-fadeIn" data-vc-animation="fadeIn"><div class="vc_gitem-zone vc_gitem-zone-a" style="height: 300px;background-image: url('https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2018/05/Hwangs-UTown-1024x684.jpg') !important;"><img src="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2018/05/Hwangs-UTown-1024x684.jpg" class="vc_gitem-zone-img" alt="Location: Town Plaza
Seating Capacity: 114
Term Time &amp; Vacation Operating Hours:
Mon-Sat, 10.30am-9.00pm
Sun closed
Contact No: 9833 0603
Nearest Carpark: CREATE Tower"><div class="vc_gitem-zone-mini"></div></div><div class="vc_gitem-zone vc_gitem-zone-b vc_custom_1526612607150 vc-gitem-zone-height-mode-auto"><div class="vc_gitem-zone-mini"></div></div></div><div class="vc_gitem-zone vc_gitem-zone-c vc_custom_1534521947044"><div class="vc_gitem-zone-mini"><div class="vc_gitem_row vc_row vc_gitem-row-position-top"><div class="vc_col-sm-12 vc_gitem-col vc_gitem-col-align-"><div class="vc_custom_heading heading-orange vc_custom_1534521762134 vc_gitem-post-data vc_gitem-post-data-source-post_title"><h3 style="text-align: left">Hwang’s Korean Restaurant</h3></div><div class="vc_custom_heading vc_custom_1534520726761 vc_gitem-post-data vc_gitem-post-data-source-post_excerpt"><p style="text-align: left"></p><p>Location: Town Plaza<br>
Seating Capacity: 114<br>
Term Time &amp; Vacation Operating Hours:<br>
Mon-Sat, 10.30am-9.00pm<br>
Sun closed<br>
Contact No: 9833 0603<br>
Nearest Carpark: CREATE Tower</p>
<p></p></div></div></div></div></div></div><div class="vc_clearfix"></div></div><div class="vc_grid-item vc_clearfix vc_col-sm-12 vc_grid-item-zone-c-right vc_visible-item fadeIn animated"><div class="vc_grid-item-mini vc_clearfix "><div class="vc_gitem-animated-block  vc_gitem-animate vc_gitem-animate-fadeIn" data-vc-animation="fadeIn"><div class="vc_gitem-zone vc_gitem-zone-a" style="height: 300px;background-image: url('https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2024/01/Bean-2-1024x660.jpg') !important;"><img src="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2024/01/Bean-2-1024x660.jpg" class="vc_gitem-zone-img" alt="Location: Town Plaza
Term Time Operating Hours:
Mon-Fri 7 am – 9 pm
Sat-Sat &amp; PH 8 am – 7 pm
Vacation Operating Hours:
Mon-Fri, 8 am – 7 pm
Weekend/PH closed
Nearest Carpark: CREATE Tower
Nearest Bus Stop: University Town"><div class="vc_gitem-zone-mini"></div></div><div class="vc_gitem-zone vc_gitem-zone-b vc_custom_1526612607150 vc-gitem-zone-height-mode-auto"><div class="vc_gitem-zone-mini"></div></div></div><div class="vc_gitem-zone vc_gitem-zone-c vc_custom_1534521947044"><div class="vc_gitem-zone-mini"><div class="vc_gitem_row vc_row vc_gitem-row-position-top"><div class="vc_col-sm-12 vc_gitem-col vc_gitem-col-align-"><div class="vc_custom_heading heading-orange vc_custom_1534521762134 vc_gitem-post-data vc_gitem-post-data-source-post_title"><h3 style="text-align: left">Mr Bean / Do Qoo</h3></div><div class="vc_custom_heading vc_custom_1534520726761 vc_gitem-post-data vc_gitem-post-data-source-post_excerpt"><p style="text-align: left"></p><p>Location: Town Plaza<br>
Term Time Operating Hours:<br>
Mon-Fri 7 am – 9 pm<br>
Sat-Sat &amp; PH 8 am – 7 pm<br>
Vacation Operating Hours:<br>
Mon-Fri, 8 am – 7 pm<br>
Weekend/PH closed<br>
Nearest Carpark: CREATE Tower<br>
Nearest Bus Stop: University Town</p>
<p></p></div></div></div></div></div></div><div class="vc_clearfix"></div></div><div class="vc_grid-item vc_clearfix vc_col-sm-12 vc_grid-item-zone-c-right vc_grid-term-76 vc_visible-item fadeIn animated"><div class="vc_grid-item-mini vc_clearfix "><div class="vc_gitem-animated-block  vc_gitem-animate vc_gitem-animate-fadeIn" data-vc-animation="fadeIn"><div class="vc_gitem-zone vc_gitem-zone-a" style="height: 300px;background-image: url('https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2018/05/Sapore-1024x684.jpg') !important;"><img src="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2018/05/Sapore-1024x684.jpg" class="vc_gitem-zone-img" alt="Location: Town Plaza
Seating Capacity: 122
Term Time Operating Hours:
Tue-Sun, 12.00pm-9.30pm
Mon, closed
Vacation Operating Hours:
Mon-Sat, 12.00pm-8.00pm
(Will be closed on 23 Dec 2022 to 9 Jan 2023)
Contact No: 6262 0287
Nearest Carpark: CREATE Tower"><div class="vc_gitem-zone-mini"></div></div><div class="vc_gitem-zone vc_gitem-zone-b vc_custom_1526612607150 vc-gitem-zone-height-mode-auto"><div class="vc_gitem-zone-mini"></div></div></div><div class="vc_gitem-zone vc_gitem-zone-c vc_custom_1534521947044"><div class="vc_gitem-zone-mini"><div class="vc_gitem_row vc_row vc_gitem-row-position-top"><div class="vc_col-sm-12 vc_gitem-col vc_gitem-col-align-"><div class="vc_custom_heading heading-orange vc_custom_1534521762134 vc_gitem-post-data vc_gitem-post-data-source-post_title"><h3 style="text-align: left">Sapore Italian Restaurant</h3></div><div class="vc_custom_heading vc_custom_1534520726761 vc_gitem-post-data vc_gitem-post-data-source-post_excerpt"><p style="text-align: left"></p><p>Location: Town Plaza<br>
Seating Capacity: 122<br>
Term Time Operating Hours:<br>
Tue-Sun, 12.00pm-9.30pm<br>
Mon, closed<br>
Vacation Operating Hours:<br>
Mon-Sat, 12.00pm-8.00pm<br>
(Will be closed on 23 Dec 2022 to 9 Jan 2023)<br>
Contact No: 6262 0287<br>
Nearest Carpark: CREATE Tower</p>
<p></p></div></div></div></div></div></div><div class="vc_clearfix"></div></div><div class="vc_grid-item vc_clearfix vc_col-sm-12 vc_grid-item-zone-c-right vc_grid-term-79 vc_visible-item fadeIn animated"><div class="vc_grid-item-mini vc_clearfix "><div class="vc_gitem-animated-block  vc_gitem-animate vc_gitem-animate-fadeIn" data-vc-animation="fadeIn"><div class="vc_gitem-zone vc_gitem-zone-a" style="height: 300px;background-image: url('https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2018/05/Starbucks-UTown-1024x684.jpg') !important;"><img src="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2018/05/Starbucks-UTown-1024x684.jpg" class="vc_gitem-zone-img" alt="Location: Education Resource Centre (ERC)
Seating Capacity: 330
Term Time &amp; Vacation Operating Hours:
Daily 8.00am to 9.00pm 
Contact: 6910 1127
Nearest Carpark: Stephen Riady Centre"><div class="vc_gitem-zone-mini"></div></div><div class="vc_gitem-zone vc_gitem-zone-b vc_custom_1526612607150 vc-gitem-zone-height-mode-auto"><div class="vc_gitem-zone-mini"></div></div></div><div class="vc_gitem-zone vc_gitem-zone-c vc_custom_1534521947044"><div class="vc_gitem-zone-mini"><div class="vc_gitem_row vc_row vc_gitem-row-position-top"><div class="vc_col-sm-12 vc_gitem-col vc_gitem-col-align-"><div class="vc_custom_heading heading-orange vc_custom_1534521762134 vc_gitem-post-data vc_gitem-post-data-source-post_title"><h3 style="text-align: left">Starbucks</h3></div><div class="vc_custom_heading vc_custom_1534520726761 vc_gitem-post-data vc_gitem-post-data-source-post_excerpt"><p style="text-align: left"></p><p>Location: Education Resource Centre (ERC)<br>
Seating Capacity: 330<br>
Term Time &amp; Vacation Operating Hours:<br>
Daily 8.00am to 9.00pm<br>
Contact: 6910 1127<br>
Nearest Carpark: Stephen Riady Centre</p>
<p></p></div></div></div></div></div></div><div class="vc_clearfix"></div></div><div class="vc_grid-item vc_clearfix vc_col-sm-12 vc_grid-item-zone-c-right vc_grid-term-77 vc_visible-item fadeIn animated"><div class="vc_grid-item-mini vc_clearfix "><div class="vc_gitem-animated-block  vc_gitem-animate vc_gitem-animate-fadeIn" data-vc-animation="fadeIn"><div class="vc_gitem-zone vc_gitem-zone-a" style="height: 300px;background-image: url('https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2022/07/Subway-1024x768.jpg') !important;"><img src="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2022/07/Subway-1024x768.jpg" class="vc_gitem-zone-img" alt="(HALAL CERTIFIED)
Location: Town Plaza
Seating Capacity: 15
Term Time &amp; Vacation Operating Hours:
Mon-Sun, 8.30am-9.30pm
Nearest Carpark: Stephen Riady Centre"><div class="vc_gitem-zone-mini"></div></div><div class="vc_gitem-zone vc_gitem-zone-b vc_custom_1526612607150 vc-gitem-zone-height-mode-auto"><div class="vc_gitem-zone-mini"></div></div></div><div class="vc_gitem-zone vc_gitem-zone-c vc_custom_1534521947044"><div class="vc_gitem-zone-mini"><div class="vc_gitem_row vc_row vc_gitem-row-position-top"><div class="vc_col-sm-12 vc_gitem-col vc_gitem-col-align-"><div class="vc_custom_heading heading-orange vc_custom_1534521762134 vc_gitem-post-data vc_gitem-post-data-source-post_title"><h3 style="text-align: left">Subway</h3></div><div class="vc_custom_heading vc_custom_1534520726761 vc_gitem-post-data vc_gitem-post-data-source-post_excerpt"><p style="text-align: left"></p><p>(HALAL CERTIFIED)<br>
Location: Town Plaza<br>
Seating Capacity: 15<br>
Term Time &amp; Vacation Operating Hours:<br>
Mon-Sun, 8.30am-9.30pm<br>
Nearest Carpark: Stephen Riady Centre</p>
<p></p></div></div></div></div></div></div><div class="vc_clearfix"></div></div><div class="vc_grid-item vc_clearfix vc_col-sm-12 vc_grid-item-zone-c-right vc_grid-term-76 vc_visible-item fadeIn animated"><div class="vc_grid-item-mini vc_clearfix "><div class="vc_gitem-animated-block  vc_gitem-animate vc_gitem-animate-fadeIn" data-vc-animation="fadeIn"><div class="vc_gitem-zone vc_gitem-zone-a" style="height: 300px;background-image: url('https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2019/10/Supersnacks-Edited-1024x684.jpg') !important;"><img src="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2019/10/Supersnacks-Edited-1024x684.jpg" class="vc_gitem-zone-img" alt="(PENDING HALAL CERT)
Location: Stephen Riady Centre
Term Time Operating Hours:
Mon-Fri, 11.00am-2.00am
Sat/Sun/PH, 6.00pm-2.00am
Nearest Carpark: Stephen Riady Centre"><div class="vc_gitem-zone-mini"></div></div><div class="vc_gitem-zone vc_gitem-zone-b vc_custom_1526612607150 vc-gitem-zone-height-mode-auto"><div class="vc_gitem-zone-mini"></div></div></div><div class="vc_gitem-zone vc_gitem-zone-c vc_custom_1534521947044"><div class="vc_gitem-zone-mini"><div class="vc_gitem_row vc_row vc_gitem-row-position-top"><div class="vc_col-sm-12 vc_gitem-col vc_gitem-col-align-"><div class="vc_custom_heading heading-orange vc_custom_1534521762134 vc_gitem-post-data vc_gitem-post-data-source-post_title"><h3 style="text-align: left">Supersnacks</h3></div><div class="vc_custom_heading vc_custom_1534520726761 vc_gitem-post-data vc_gitem-post-data-source-post_excerpt"><p style="text-align: left"></p><p>(PENDING HALAL CERT)<br>
Location: Stephen Riady Centre<br>
Term Time Operating Hours:<br>
Mon-Fri, 11.00am-2.00am<br>
Sat/Sun/PH, 6.00pm-2.00am<br>
Nearest Carpark: Stephen Riady Centre</p>
<p></p></div></div></div></div></div></div><div class="vc_clearfix"></div></div><div class="vc_grid-item vc_clearfix vc_col-sm-12 vc_grid-item-zone-c-right vc_grid-term-77 vc_grid-term-76 vc_visible-item fadeIn animated"><div class="vc_grid-item-mini vc_clearfix "><div class="vc_gitem-animated-block  vc_gitem-animate vc_gitem-animate-fadeIn" data-vc-animation="fadeIn"><div class="vc_gitem-zone vc_gitem-zone-a" style="height: 300px;background-image: url('https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2018/05/The-Royals-Cafe-1024x684.jpg') !important;"><img src="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2018/05/The-Royals-Cafe-1024x684.jpg" class="vc_gitem-zone-img" alt="(HALAL CERTIFIED)
Location: Town Plaza
Seating Capacity: 60
Term Time &amp; Vacation Operating Hours:
Mon-Sat, 11.00am-8.00pm
Sun/PH closed
(Will be closed on 29 Dec 2022 - 2 Jan 2023)
Contact: 97771353
Nearest Carpark: CREATE Tower"><div class="vc_gitem-zone-mini"></div></div><div class="vc_gitem-zone vc_gitem-zone-b vc_custom_1526612607150 vc-gitem-zone-height-mode-auto"><div class="vc_gitem-zone-mini"></div></div></div><div class="vc_gitem-zone vc_gitem-zone-c vc_custom_1534521947044"><div class="vc_gitem-zone-mini"><div class="vc_gitem_row vc_row vc_gitem-row-position-top"><div class="vc_col-sm-12 vc_gitem-col vc_gitem-col-align-"><div class="vc_custom_heading heading-orange vc_custom_1534521762134 vc_gitem-post-data vc_gitem-post-data-source-post_title"><h3 style="text-align: left">The Royals Bistro</h3></div><div class="vc_custom_heading vc_custom_1534520726761 vc_gitem-post-data vc_gitem-post-data-source-post_excerpt"><p style="text-align: left"></p><p>(HALAL CERTIFIED)<br>
Location: Town Plaza<br>
Seating Capacity: 60<br>
Term Time &amp; Vacation Operating Hours:<br>
Mon-Sat, 11.00am-8.00pm<br>
Sun/PH closed<br>
(Will be closed on 29 Dec 2022 – 2 Jan 2023)<br>
Contact: 97771353<br>
Nearest Carpark: CREATE Tower</p>
<p></p></div></div></div></div></div></div><div class="vc_clearfix"></div></div><div class="vc_grid-item vc_clearfix vc_col-sm-12 vc_grid-item-zone-c-right vc_visible-item fadeIn animated"><div class="vc_grid-item-mini vc_clearfix "><div class="vc_gitem-animated-block  vc_gitem-animate vc_gitem-animate-fadeIn" data-vc-animation="fadeIn"><div class="vc_gitem-zone vc_gitem-zone-a" style="height: 300px;background-image: url('https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2022/08/Triplets-1024x768.jpg') !important;"><img src="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2022/08/Triplets-1024x768.jpg" class="vc_gitem-zone-img" alt="(PENDING HALAL CERT)
Location: UTown Stephen Riady Centre (SRC)
Seating Capacity: 8
Term Time &amp; Vacation Operating Hours:
Mon-Sun: 8.00am to 8.00pm
Nearest Carpark: CREATE Tower"><div class="vc_gitem-zone-mini"></div></div><div class="vc_gitem-zone vc_gitem-zone-b vc_custom_1526612607150 vc-gitem-zone-height-mode-auto"><div class="vc_gitem-zone-mini"></div></div></div><div class="vc_gitem-zone vc_gitem-zone-c vc_custom_1534521947044"><div class="vc_gitem-zone-mini"><div class="vc_gitem_row vc_row vc_gitem-row-position-top"><div class="vc_col-sm-12 vc_gitem-col vc_gitem-col-align-"><div class="vc_custom_heading heading-orange vc_custom_1534521762134 vc_gitem-post-data vc_gitem-post-data-source-post_title"><h3 style="text-align: left">Triplets</h3></div><div class="vc_custom_heading vc_custom_1534520726761 vc_gitem-post-data vc_gitem-post-data-source-post_excerpt"><p style="text-align: left"></p><p>(PENDING HALAL CERT)<br>
Location: UTown Stephen Riady Centre (SRC)<br>
Seating Capacity: 8<br>
Term Time &amp; Vacation Operating Hours:<br>
Mon-Sun: 8.00am to 8.00pm<br>
Nearest Carpark: CREATE Tower</p>
<p></p></div></div></div></div></div></div><div class="vc_clearfix"></div></div><div class="vc_grid-item vc_clearfix vc_col-sm-12 vc_grid-item-zone-c-right vc_grid-term-74 vc_visible-item fadeIn animated"><div class="vc_grid-item-mini vc_clearfix "><div class="vc_gitem-animated-block  vc_gitem-animate vc_gitem-animate-fadeIn" data-vc-animation="fadeIn"><div class="vc_gitem-zone vc_gitem-zone-a" style="height: 300px;background-image: url('https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2020/01/Udon-1024x689.jpg') !important;"><img src="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2020/01/Udon-1024x689.jpg" class="vc_gitem-zone-img" alt="Location: Town Plaza
Seating Capacity:
Term Time Operating Hours:
Mon-Sun: 11.00am-9.30pm
Vacation Operating Hours:
Mon-Sun: 11.00am-9.00pm
Contact: 66946240
Nearest Carpark: CREATE Tower"><div class="vc_gitem-zone-mini"></div></div><div class="vc_gitem-zone vc_gitem-zone-b vc_custom_1526612607150 vc-gitem-zone-height-mode-auto"><div class="vc_gitem-zone-mini"></div></div></div><div class="vc_gitem-zone vc_gitem-zone-c vc_custom_1534521947044"><div class="vc_gitem-zone-mini"><div class="vc_gitem_row vc_row vc_gitem-row-position-top"><div class="vc_col-sm-12 vc_gitem-col vc_gitem-col-align-"><div class="vc_custom_heading heading-orange vc_custom_1534521762134 vc_gitem-post-data vc_gitem-post-data-source-post_title"><h3 style="text-align: left">Udon Don Bar</h3></div><div class="vc_custom_heading vc_custom_1534520726761 vc_gitem-post-data vc_gitem-post-data-source-post_excerpt"><p style="text-align: left"></p><p>Location: Town Plaza<br>
Seating Capacity:<br>
Term Time Operating Hours:<br>
Mon-Sun: 11.00am-9.30pm<br>
Vacation Operating Hours:<br>
Mon-Sun: 11.00am-9.00pm<br>
Contact: 66946240<br>
Nearest Carpark: CREATE Tower</p>
<p></p></div></div></div></div></div></div><div class="vc_clearfix"></div></div><div class="vc_grid-item vc_clearfix vc_col-sm-12 vc_grid-item-zone-c-right vc_grid-term-74 vc_visible-item fadeIn animated"><div class="vc_grid-item-mini vc_clearfix "><div class="vc_gitem-animated-block  vc_gitem-animate vc_gitem-animate-fadeIn" data-vc-animation="fadeIn"><div class="vc_gitem-zone vc_gitem-zone-a" style="height: 300px;background-image: url('https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2018/05/Waa-Cow-1-1024x684.jpg') !important;"><img src="https://uci.nus.edu.sg/oca/wp-content/uploads/sites/9/2018/05/Waa-Cow-1-1024x684.jpg" class="vc_gitem-zone-img" alt="Location: Stephen Riady Centre (SRC)
Term Time Operating Hours: 
Mon-Fri, 11.30am-8.30pm
Sat/Sun/PH, 12.00pm-8.30pm
Vacation Operating Hours:
Mon-Fri, 11.30am-8.30pm
Sat/Sun/PH, 12.00pm-8.30pm
Contact: 82230550
Nearest Carpark: Stephen Riady Centre"><div class="vc_gitem-zone-mini"></div></div><div class="vc_gitem-zone vc_gitem-zone-b vc_custom_1526612607150 vc-gitem-zone-height-mode-auto"><div class="vc_gitem-zone-mini"></div></div></div><div class="vc_gitem-zone vc_gitem-zone-c vc_custom_1534521947044"><div class="vc_gitem-zone-mini"><div class="vc_gitem_row vc_row vc_gitem-row-position-top"><div class="vc_col-sm-12 vc_gitem-col vc_gitem-col-align-"><div class="vc_custom_heading heading-orange vc_custom_1534521762134 vc_gitem-post-data vc_gitem-post-data-source-post_title"><h3 style="text-align: left">Waa Cow</h3></div><div class="vc_custom_heading vc_custom_1534520726761 vc_gitem-post-data vc_gitem-post-data-source-post_excerpt"><p style="text-align: left"></p><p>Location: Stephen Riady Centre (SRC)<br>
Term Time Operating Hours:<br>
Mon-Fri, 11.30am-8.30pm<br>
Sat/Sun/PH, 12.00pm-8.30pm<br>
Vacation Operating Hours:<br>
Mon-Fri, 11.30am-8.30pm<br>
Sat/Sun/PH, 12.00pm-8.30pm<br>
Contact: 82230550<br>
Nearest Carpark: Stephen Riady Centre</p>
<p></p></div></div></div></div></div></div><div class="vc_clearfix"></div></div></div></div>
	</div>
</div></div></div></div><div class="wpb_column vc_column_container vc_col-sm-4"><div class="vc_column-inner vc_custom_1524725489751"><div class="wpb_wrapper"><div class="vc_wp_custommenu wpb_content_element nus-right-sidebar"><div class="widget widget_nav_menu"><nav class="menu-retail-dining-container" aria-label="Menu"><ul id="menu-retail-dining" class="menu"><li id="menu-item-399" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-399"><a href="https://uci.nus.edu.sg/oca/retail-dining/introduction/" class="menu-link">Introduction</a></li>
<li id="menu-item-398" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-398"><a href="https://uci.nus.edu.sg/oca/retail-dining/food-and-beverages/" class="menu-link">Food and Beverages</a></li>
<li id="menu-item-397" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-397"><a href="https://uci.nus.edu.sg/oca/retail-dining/retail/" class="menu-link">Retail</a></li>
<li id="menu-item-6307" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6307"><a href="https://uci.nus.edu.sg/oca/faqs/retail-and-dining/rds-new-leasing-opportunities/" class="menu-link">New Leasing opportunities</a></li>
<li id="menu-item-6489" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6489"><a href="https://uci.nus.edu.sg/oca/campus-food-delivery/" class="menu-link">Campus Food Delivery</a></li>
<li id="menu-item-6488" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-6488"><a href="https://uci.nus.edu.sg/oca/retail-dining/well-certification/" class="menu-link">WELL Certification</a></li>
</ul></nav></div></div></div></div></div></div>
</section>
	
	
</div><!-- .entry-content .clear -->

	
	
</article><!-- #post-## -->

			</main><!-- #main -->
			
		
	</div><!-- #primary -->


	</div> <!-- ast-container -->
	</div><!-- #content -->

		<footer class="site-footer" id="colophon" itemtype="https://schema.org/WPFooter" itemscope="itemscope" itemid="#colophon">

			
			
<!-- NUS BREADCRUMBS - START -->
<div class="nus-breadcrumbs">
	<div class="ast-container">
		<ul><li class="item-home"><span class="icon faicon fa-map-marker"></span><a class="bread-link bread-home" href="https://uci.nus.edu.sg/oca" title="Homepage">Homepage</a></li><li class="item-parent item-parent-380"><a class="bread-parent bread-parent-380" href="https://uci.nus.edu.sg/oca/retail-dining/" title="Retail &amp; Dining">Retail &amp; Dining</a></li><li class="item-current item-1010"><strong title="Food and Beverage – UTown"> Food and Beverage – UTown</strong></li></ul>	</div>
</div>
<!-- NUS BREADCRUMBS - END -->

<div class="footer-adv footer-adv-layout-4 nus-footer">
	<div class="footer-adv-overlay nus-footer-overlay">
		<div class="ast-container">
			<div class="ast-row navigator">
				<div class="ast-col-lg-12 ast-col-md-12 ast-col-sm-12 ast-col-xs-12 nus-footer-widget">

					<div class="ast-row">
						<div class="ast-col-lg-12 ast-col-md-12 ast-col-sm-12 ast-col-xs-12 footer-adv-widget footer-adv-widget-1 nus-footer-right-text">
							<div id="custom_html-2" class="widget_text widget widget_custom_html"><div class="textwidget custom-html-widget"><div class="nus-social-box">
    <div class="nus-module module">
        <div class="module-inner">
            <h3 class="title">Campus Life (Campus Services)</h3>
                <div class="module-ct">
                    <ul class="nus-contact-us">
                        <li>
							<span class="icon fa fa-location-arrow"></span>
							8 Kent Ridge Drive, #02-03<br>
							Singapore 119246
						</li>
                        <li>
							<span class="icon fa fa-phone"></span>
							+65 6601 7878 
						</li>
                        <li>
							<span class="icon fa fa-envelope"></span>
							<a href="mailto:csenquiry@nus.edu.sg">csenquiry@nus.edu.sg</a>
						</li>
                    </ul>
                </div>
            </div>
			<div class="nus-module module footnav-alt">
            <div class="module-inner">
                <div class="module-ct">
                    <div>
                     
                        <a target="_blank" href="https://www.instagram.com/nus_oca/" rel="noopener noreferrer"><img width="32" height="32" alt="instagram" src="/wp-content/themes/nus-astra/assets/images/instagram.png"></a>&nbsp;
                    </div>
                </div>
            </div>
        </div>
        </div>
    </div>
</div></div>						</div>
					</div>

				</div><!-- .nus-footer-widget -->
			</div><!-- .ast-row -->
		</div><!-- .ast-container -->
	</div><!-- .footer-adv-overlay-->
</div><!-- .ast-theme-footer .footer-adv-layout-4 -->

<div class="ast-small-footer footer-sml-layout-1">
	<div class="ast-footer-overlay">
		<div class="ast-container">
			<div class="ast-small-footer-wrap">
									<div class="ast-small-footer-section ast-small-footer-section-1">
						Copyright © 2024 <span class="ast-footer-site-title">Campus Services</span> | Powered by Websparks					</div>
				
				
			</div><!-- .ast-row .ast-small-footer-wrap -->
		</div><!-- .ast-container -->
	</div><!-- .ast-footer-overlay -->
</div><!-- .ast-small-footer-->

			
		</footer><!-- #colophon -->
			</div><!-- #page -->

		<script>
			window.RS_MODULES = window.RS_MODULES || {};
			window.RS_MODULES.modules = window.RS_MODULES.modules || {};
			window.RS_MODULES.waiting = window.RS_MODULES.waiting || [];
			window.RS_MODULES.defered = true;
			window.RS_MODULES.moduleWaiting = window.RS_MODULES.moduleWaiting || {};
			window.RS_MODULES.type = 'compiled';
		</script>
		            <div id="watsonconv-floating-box"></div>
        <link rel="stylesheet" id="lightbox2-css" href="https://uci.nus.edu.sg/oca/wp-content/plugins/js_composer/assets/lib/lightbox2/dist/css/lightbox.min.css?ver=7.0" media="all">
<link rel="stylesheet" id="vc_pageable_owl-carousel-css-css" href="https://uci.nus.edu.sg/oca/wp-content/plugins/js_composer/assets/lib/owl-carousel2-dist/assets/owl.min.css?ver=7.0" media="all">
<link rel="stylesheet" id="vc_animate-css-css" href="https://uci.nus.edu.sg/oca/wp-content/plugins/js_composer/assets/lib/bower/animate-css/animate.min.css?ver=7.0" media="all">
<link rel="stylesheet" id="rs-plugin-settings-css" href="https://uci.nus.edu.sg/oca/wp-content/plugins/revslider/public/assets/css/rs6.css?ver=6.6.16" media="all">
<style id="rs-plugin-settings-inline-css">
#rs-demo-id {}
</style>
<script id="astra-theme-js-js-extra">
var astra = {"break_point":"921","isRtl":"","is_scroll_to_id":"","is_scroll_to_top":"","is_header_footer_builder_active":""};
</script>
<script src="https://uci.nus.edu.sg/oca/wp-content/themes/astra/assets/js/minified/style.min.js?ver=4.4.1" id="astra-theme-js-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-content/plugins/revslider/public/assets/js/rbtools.min.js?ver=6.6.16" defer="" async="" id="tp-tools-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-content/plugins/revslider/public/assets/js/rs6.min.js?ver=6.6.16" defer="" async="" id="revmin-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-content/themes/nus-astra/assets/js/main.js?ver=20180228" id="nus-astra-navigation-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-content/plugins/js_composer/assets/js/dist/js_composer_front.min.js?ver=7.0" id="wpb_composer_front_js-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-content/plugins/js_composer/assets/lib/lightbox2/dist/js/lightbox.min.js?ver=7.0" id="lightbox2-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-content/plugins/js_composer/assets/lib/owl-carousel2-dist/owl.carousel.min.js?ver=7.0" id="vc_pageable_owl-carousel-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-content/plugins/js_composer/assets/lib/bower/imagesloaded/imagesloaded.pkgd.min.js?ver=7.0" id="vc_grid-js-imagesloaded-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-includes/js/underscore.min.js?ver=1.13.4" id="underscore-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-content/plugins/js_composer/assets/lib/vc_waypoints/vc-waypoints.min.js?ver=7.0" id="vc_waypoints-js"></script>
<script src="https://uci.nus.edu.sg/oca/wp-content/plugins/js_composer/assets/js/dist/vc_grid.min.js?ver=7.0" id="vc_grid-js"></script>
			<script>
			/(trident|msie)/i.test(navigator.userAgent)&&document.getElementById&&window.addEventListener&&window.addEventListener("hashchange",function(){var t,e=location.hash.substring(1);/^[A-z0-9_-]+$/.test(e)&&(t=document.getElementById(e))&&(/^(?:a|select|input|button|textarea)$/i.test(t.tagName)||(t.tabIndex=-1),t.focus())},!1);
			</script>
			<script></script>	

<div id="lightboxOverlay" tabindex="-1" class="lightboxOverlay" style="display: none;"></div><div id="lightbox" tabindex="-1" class="lightbox" style="display: none;"><div class="lb-outerContainer"><div class="lb-container"><img class="lb-image" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==" alt=""><div class="lb-nav"><a class="lb-prev" aria-label="Previous image" href=""></a><a class="lb-next" aria-label="Next image" href=""></a></div><div class="lb-loader"><a class="lb-cancel"></a></div></div></div><div class="lb-dataContainer"><div class="lb-data"><div class="lb-details"><span class="lb-caption"></span><span class="lb-number"></span></div><div class="lb-closeContainer"><a class="lb-close"></a></div></div></div></div></body>""","UTown"]

    # Add more URLs if needed
]

# Initialize an empty list to hold all stores data
stores_data = []

for url in urls:
    # Send a GET request to the page
    page,location = url

    
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(page, 'html.parser')
    print(soup)
    # Find elements containing the store information
    # Note: The selectors used here are hypothetical and may not work for the actual web page. They must be adjusted to fit the page's structure.
    store_elements = soup.select('div.store-info')  # Hypothetical selector, change based on actual page structure
    
    for element in store_elements:
        # Extract store details
        store_name = element.select_one('.store-name').text.strip()  # Hypothetical selector
        # location = element.select_one('.store-location').text.strip()  # Hypothetical selector
        opening_hours = element.select_one('.store-opening-hours').text.strip()  # Hypothetical selector
        
        # Assuming vegetarian information is not available on the webpage and setting it to False by default
        vegetarian = False
        
        # Append the store details to the list
        stores_data.append({
            "storeName": store_name,
            "location": location,
            "vegetarian": vegetarian,
            "openingHours": opening_hours
        })

# Write the data to a JSON file
with open('storesData.json', 'w') as json_file:
    json.dump(stores_data, json_file, indent=4)

print("Data scraped and saved to storesData.json")