# -*- coding: utf-8 -*- 
import formFile
class download:
	result=""
	sessionDic=dict()
	def __init__(self,param,pyFile,session,headerInfo,lattedb):
		self.generate(param,pyFile,session,headerInfo,lattedb)

	def generate(self,param,pyFile,session,headerInfo,lattedb):

		self.result+=str("""<!DOCTYPE html>
		 """)
		self.result+=str("""<html>
			 """)
		self.result+=str("""<head>
			 """)
		self.result+=str("""<meta name="viewport" content="width=device-width, initial-scale=1">
			 """)
		self.result+=str("""<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
			 """)
		self.result+=str("""<title>Pylatte - Web framework based on Python3 """)
		self.result+=str("""</title>
			
			 """)
		self.result+=str("""<!-- favicon -->
			 """)
		self.result+=str("""<link rel="shortcut icon" href="../pyl/favicon.ico" type="image/x-icon">
			 """)
		self.result+=str("""<link rel="icon" href="../pyl/favicon.ico" type="image/x-icon">
		
			 """)
		self.result+=str("""<!-- Include required JS files -->
			 """)
		self.result+=str("""<script type="text/javascript" src="../pyl/syntaxhighlighter/js/xregexp.js"> """)
		self.result+=str("""</script>
			 """)
		self.result+=str("""<script type="text/javascript" src="../pyl/syntaxhighlighter/js/shCore.js"> """)
		self.result+=str("""</script>
			 
			 """)
		self.result+=str("""<!--
			    At least one brush, here we choose JS. You need to include a brush for every
			    language you want to highlight
			-->
			 """)
		self.result+=str("""<script type="text/javascript" src="../pyl/syntaxhighlighter/lang/shBrushXml.js"> """)
		self.result+=str("""</script>
			 """)
		self.result+=str("""<script type="text/javascript" src="../pyl/syntaxhighlighter/lang/shBrushBash.js"> """)
		self.result+=str("""</script>
			 
			 """)
		self.result+=str("""<!-- Include *at least* the core style and default theme -->
			 """)
		self.result+=str("""<link href="../pyl/syntaxhighlighter/css/shCore.css" rel="stylesheet" type="text/css" />
			 """)
		self.result+=str("""<link href="../pyl/syntaxhighlighter/css/shThemeDefault.css" rel="stylesheet" type="text/css" />
			
			
			
			 """)
		self.result+=str("""<link rel="stylesheet"  href="../pyl/css/jquery.mobile-1.0rc2.css"/>
			 """)
		self.result+=str("""<link rel="stylesheet"  href="../pyl/css/jqm-docs.css"/>
			
			 """)
		self.result+=str("""<script src="../pyl/js/jquery-1.6.4.min.js"> """)
		self.result+=str("""</script>
			 """)
		self.result+=str("""<script src="../pyl/js/jqm-docs.js"> """)
		self.result+=str("""</script>
			 """)
		self.result+=str("""<script src="../pyl/js/jquery.mobile.themeswitcher.js"> """)
		self.result+=str("""</script>
			 """)
		self.result+=str("""<script src="../pyl/js/jquery.mobile-1.0rc2.js"> """)
		self.result+=str("""</script>
			
			 """)
		self.result+=str("""<script type="text/javascript">
		
			  var _gaq = _gaq || [];
			  _gaq.push(['_setAccount', 'UA-26668199-1']);
			  _gaq.push(['_trackPageview']);
			
			  (function() {
			    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
			    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
			    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
			  })();
			
			 """)
		self.result+=str("""</script>
			
			 """)
		self.result+=str("""</head>
		
		 """)
		self.result+=str("""<body>
		
			 """)
		self.result+=str("""<div data-role="page" class="type-interior">
		
				 """)
		self.result+=str("""<div data-role="header" data-theme="b">
				 """)
		self.result+=str("""<h1>Pylatte Official Webpage """)
		self.result+=str("""</h1>
				 """)
		self.result+=str("""<a href="../../" target="_self" data-icon="home" data-iconpos="notext" data-direction="reverse" class="ui-btn-right jqm-home">Home """)
		self.result+=str("""</a>
			 """)
		self.result+=str("""</div> """)
		self.result+=str("""<!-- /header -->
		
			 """)
		self.result+=str("""<div data-role="content">
					 """)
		self.result+=str("""<div class="content-primary">
					 """)
		self.result+=str("""<h1>Download """)
		self.result+=str("""</h1>
					 """)
		self.result+=str("""<h2>Downloading Pylatte """)
		self.result+=str("""</h2>
						 """)
		self.result+=str("""<ul>
							 """)
		self.result+=str("""<li> """)
		self.result+=str("""<h3>Released Code """)
		self.result+=str("""</h3> """)
		self.result+=str("""</li>
							 """)
		self.result+=str("""<p>Latest stable release :  """)
		self.result+=str("""<a href = "http://code.google.com/p/pylatte/downloads/list" target="_blank">ver 0.9.0 """)
		self.result+=str("""</a> """)
		self.result+=str("""</p>
							 """)
		self.result+=str("""<p>This is Released code for user who would like to develop website using pylatte.
					
							 """)
		self.result+=str("""<li> """)
		self.result+=str("""<h3>Development code """)
		self.result+=str("""</h3> """)
		self.result+=str("""</li>
							 """)
		self.result+=str("""<p>Latest development code :  """)
		self.result+=str("""<a href = "http://code.google.com/p/pylatte/" target="_blank">ver 0.9.0 """)
		self.result+=str("""</a> """)
		self.result+=str("""</p>
							 """)
		self.result+=str("""<o>This is Development code for developer who would like to join Pylatte development with us. Anyone who is interested in development of Pylatte is welcome. Join us now.
						 """)
		self.result+=str("""</ul>
					 """)
		self.result+=str("""<h2>Extra Modules """)
		self.result+=str("""</h2>
						 """)
		self.result+=str("""<ul>
							 """)
		self.result+=str("""<li> """)
		self.result+=str("""<h3>Mysqldb for python3 """)
		self.result+=str("""</h3> """)
		self.result+=str("""</li>
							 """)
		self.result+=str("""<p>Latest stable release :  """)
		self.result+=str("""<a href = "https://github.com/davispuh/MySQL-for-Python-3" target="_blank">ver 3.6.2 """)
		self.result+=str("""</a> """)
		self.result+=str("""</p>
							 """)
		self.result+=str("""<p>Some people who are very kind alreay made mysqldb module for python3. This module is absoluately essential to use Pylatte with Mysql. If you need to use DB on your website based on Pylatte, you must download. """)
		self.result+=str("""</p>
						 """)
		self.result+=str("""</ul>
		
					 """)
		self.result+=str("""</div> """)
		self.result+=str("""<!--/content-primary -->
		
					 """)
		self.result+=str("""<div class="content-secondary">
		
						 """)
		self.result+=str("""<div data-role="collapsible" data-collapsed="true" data-theme="b" data-content-theme="d">
		
								 """)
		self.result+=str("""<h3>More in this section """)
		self.result+=str("""</h3>
		
								 """)
		self.result+=str("""<ul data-role="listview" data-theme="c" data-dividertheme="d">
									 """)
		self.result+=str("""<li data-role="list-divider">Menu """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<li> """)
		self.result+=str("""<a target="_self" href="../index">About """)
		self.result+=str("""</a> """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<li data-theme="b"> """)
		self.result+=str("""<a target="_self" href="../download">Download """)
		self.result+=str("""</a> """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<li> """)
		self.result+=str("""<a target="_self" href="../install">Install """)
		self.result+=str("""</a> """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<li> """)
		self.result+=str("""<a target="_self" href="../tutorial">Tutorial """)
		self.result+=str("""</a> """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<li> """)
		self.result+=str("""<a target="_self" href="../documentation">Documentation """)
		self.result+=str("""</a> """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<li> """)
		self.result+=str("""<a target="_self" href="../comment">Comment """)
		self.result+=str("""</a> """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<li> """)
		self.result+=str("""<a target="_self" href="../faq">F A Q """)
		self.result+=str("""</a> """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<li> """)
		self.result+=str("""<a target="_self" href="../contactus">Contact us """)
		self.result+=str("""</a> """)
		self.result+=str("""</li>
									 """)
		self.result+=str("""<img src="../pyl/image/pylatte.png"> """)
		self.result+=str("""</img>
								 """)
		self.result+=str("""</ul>
						 """)
		self.result+=str("""</div>
					 """)
		self.result+=str("""</div>
		
				 """)
		self.result+=str("""</div> """)
		self.result+=str("""<!-- /content -->
		
				 """)
		self.result+=str("""<div data-role="footer" class="footer-docs" data-theme="b">
						 """)
		self.result+=str("""<h4>&copy; 2011 The Pylatte Project """)
		self.result+=str("""</h4>
				 """)
		self.result+=str("""</div>
		
				 """)
		self.result+=str("""</div> """)
		self.result+=str("""<!-- /page -->
		
			 """)
		self.result+=str("""</body>
		 """)
		self.result+=str("""</html>
		
		
		 """)
		self.sessionDic=session
		pass
	def getHtml(self):
		return self.result
		pass
	def getSession(self):
		return self.sessionDic
		pass
