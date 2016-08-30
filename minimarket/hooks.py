# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "minimarket"
app_title = "Minimarket"
app_publisher = "ahmad"
app_description = "MiniMarket"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ahmad18189@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/minimarket/css/minimarket.css"
# app_include_js = "/assets/minimarket/js/minimarket.js"

# include js, css files in header of web template
# web_include_css = "/assets/minimarket/css/minimarket.css"
# web_include_js = "/assets/minimarket/js/minimarket.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "minimarket.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "minimarket.install.before_install"
# after_install = "minimarket.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "minimarket.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"minimarket.tasks.all"
# 	],
# 	"daily": [
# 		"minimarket.tasks.daily"
# 	],
# 	"hourly": [
# 		"minimarket.tasks.hourly"
# 	],
# 	"weekly": [
# 		"minimarket.tasks.weekly"
# 	]
# 	"monthly": [
# 		"minimarket.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "minimarket.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "minimarket.event.get_events"
# }

