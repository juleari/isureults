import urllib
from IsuHTMLParser import IsuHTMLParser
from helper import ISU_EVENT_LINK

from ISUCategory import get_category
from Shedule import get_shedule

class Event:
    '''
    ISU event information
    @url {string} -- url at isuresults
    @name {string}
    @group {string} -- name of group of competitions

    Place
    @city {string}
    @nati {string} -- country code

    Date
    @date_start
    @date_end
    @season {(int, int)} -- years of season
    @shedule {Shedule}

    People
    @participants {[ISUCategory]} -- lists of participants by categories
    '''
    def __init__(self, url, parser):
        self.url = url
        self.name = parser.name
        # self.group

        self.city = parser.city
        self.nati = parser.nati

        self.date_start = parser.start
        self.date_end = parser.end
        # self.season = self.calc_season()
        # self.shedule = self.get_shedule(links)

        links = parser.a_list
        self.participants = self.get_participants(links)

    def get_participants(self, links):
        """
        Gets participants by categories
        @param {[Link]} links
        @return {[ISUCategory]}
        """
        return map(get_category, [link for link in links if link.id == 'cat'])

    def get_shedule(self, links):
        """
        Gets shedule from pdf
        @param {[Link]} links
        @return {Schedule}
        """
        for link in links:
            if link.id == 'url' and 'schedules' in link.url:
                return get_shedule(link.url)

        return None

    def count_time(self, local_time):
        """
        Counts time in Moscow (+3)
        @param {} local_time
        @return moscow_time
        """
        print 'time', local_time
        return local_time

    def __repr__(self):
        org_info = 'name:  %s\nplace: %s, %s\ndates: %s - %s\n' %\
            (self.name, self.city, self.nati, self.date_start, self.date_end)

        participants_info = 'participants:\n' +\
                            str.join('\n', map(repr, self.participants))

        return org_info + participants_info

def get_event_info(event_number):
    """
    Returns event information from isuresults.
    Link to event page looks like:
    'http://www.isuresults.com/events/fsevent00051793.htm'
    where 00051793 -- number of the event.

    @param {string} event_number
    @return {Event}
    """
    url = '%sfsevent%s.htm' % (ISU_EVENT_LINK, event_number)
    url_html = urllib.urlopen(url).read()
    # url_html = '\r\n\r\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\r\n\r\n<html xmlns="http://www.w3.org/1999/xhtml" >\r\n<head><title>\r\n\tEvent Overview\r\n</title><link href="../../App_Themes/Default/StyleSheet.css" type="text/css" rel="stylesheet" /><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /><link type="text/css" rel="stylesheet" href="Stylesheet.css" /><link type="text/css" rel="stylesheet" href="StyleSheet.css" /><link type="text/css" rel="stylesheet" href="../../Stylesheet.css" /><link type="text/css" rel="stylesheet" href="../../StyleSheet.css" /></head>\r\n<body>\r\n    <form name="form1" method="post" action="eventOverview.aspx?selectedEventUID=d1158e3c-0226-4686-a8d4-78f8e900199c&amp;task=ZIP" id="form1">\r\n<div>\r\n<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPaA8FDzhkNDQ5MTliY2I4MWIzORgCBSJGb3JtVmlldzEkR3JpZFZpZXdfRXZlbnRDYXRlZ29yaWVzDzwrAAoBCAIBZAUJRm9ybVZpZXcxDxQrAAdkZGRkZBYAAgFkKYqjjzpDbMX47WcW4JPBmYQDMQk=" />\r\n</div>\r\n\r\n<div>\r\n\r\n\t<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="D597B6B5" />\r\n</div>\r\n    <div>\r\n        \r\n        <table cellspacing="0" border="0" id="FormView1" style="width:450px;border-collapse:collapse;">\r\n\t<tr>\r\n\t\t<td colspan="2">\r\n                <table width="100%">\r\n                    <tr>\r\n                        <td>\r\n                <span id="FormView1_event_nameLabel" class="eventOverviewHeadline1">ISU Four Continents Championships 2017</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td>\r\n                <span id="FormView1_event_sub_type_nameLabel" class="eventOverviewHeadline2">Four Continents Championships</span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td>\r\n                <span class="eventOverviewHeadline4"><span id="FormView1_event_cityLabel">Gangneung</span>\r\n                /\r\n                <span id="FormView1_event_nationLabel">KOR</span></span></td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td>\r\n                            <span class="eventOverviewHeadline3">\r\n                                <span id="FormView1_event_start_dateLabel">15.02.2017</span>\r\n                                -\r\n                                <span id="FormView1_event_end_dateLabel">19.02.2017</span>\r\n                            </span>\r\n                        </td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td>\r\n                            <hr />\r\n                        </td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td style="height: 16px">\r\n                           \r\n                            <div>\r\n\t\t\t<table cellspacing="0" border="0" id="FormView1_GridView_EventCategories" style="border-style:None;border-collapse:collapse;">\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th scope="col">&nbsp;</th>\r\n\t\t\t\t</tr><tr>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t<a id="FormView1_GridView_EventCategories_ctl02_HyperLink1" class="eventOverviewLinks" href="cat00028804.htm">Men</a>\r\n\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t</tr><tr>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t<a id="FormView1_GridView_EventCategories_ctl03_HyperLink1" class="eventOverviewLinks" href="cat00028805.htm">Ladies</a>\r\n\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t</tr><tr>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t<a id="FormView1_GridView_EventCategories_ctl04_HyperLink1" class="eventOverviewLinks" href="cat00028806.htm">Pairs</a>\r\n\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t</tr><tr>\r\n\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t\t\t\t<a id="FormView1_GridView_EventCategories_ctl05_HyperLink1" class="eventOverviewLinks" href="cat00028807.htm">Ice Dance</a>\r\n\t\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t</tr>\r\n\t\t\t</table>\r\n\t\t</div>\r\n                        </td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td>\r\n                            <hr />\r\n                            <span class="eventOverviewHeadline3"> <span id="FormView1_Label_LinksHeadline">Links:</span></span>\r\n                            <br />\r\n                            \r\n                           <table id="FormView1_DataList_EventUrls" cellspacing="0" border="0" style="border-collapse:collapse;">\r\n\t\t\t<tr>\r\n\t\t\t\t<td>\r\n                                    <a id="FormView1_DataList_EventUrls_ctl00_HyperLink_EventUrls" class="eventOverviewLinks" href="http://www.isu.org" target="_blank">ISU Homepage</a>\r\n                                    <br />\r\n                                </td>\r\n\t\t\t</tr><tr>\r\n\t\t\t\t<td>\r\n                                    <a id="FormView1_DataList_EventUrls_ctl01_HyperLink_EventUrls" class="eventOverviewLinks" href="http://www.isuresults.org/schedules/fc2017_ColouredTimeSchedule.pdf" target="_blank">Time and Practice Schedule</a>\r\n                                    <br />\r\n                                </td>\r\n\t\t\t</tr>\r\n\t\t</table>\r\n                        </td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td>\r\n                        </td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td>\r\n                        </td>\r\n                    </tr>\r\n                    <tr>\r\n                        <td>\r\n                        </td>\r\n                    </tr>\r\n                </table>\r\n                <br /><span class="eventOverviewHeadline4"></span>\r\n            </td>\r\n\t</tr>\r\n</table>\r\n        <br />\r\n        30.01.2017 14:10:25\r\n    </div>\r\n    </form>\r\n</body>\r\n</html>\r\n'

    parser = IsuHTMLParser()
    parser.feed(url_html)
    return Event(url, parser)
