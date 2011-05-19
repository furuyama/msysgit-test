# -*- coding:utf-8 -*-

import wsgiref.handlers
import logging
from google.appengine.ext import webapp
from google.appengine.api import xmpp

class XmppSend(webapp.RequestHandler):
  def get(self):
    to_address = "Gmail Address Of Destination" #送信先のGmailアドレスをここに入力
    chat_message_sent = False

    xmpp.send_invite(to_address) #招待されてる、されていないにかかわらず送信先ユーザに招待状を送る

    if xmpp.get_presence(to_address): #送信先がオンラインの場合
      msg = "I'm Google Talk bot!"
      status_code = xmpp.send_message(to_address, msg)
      chat_message_sent = (status_code == xmpp.NO_ERROR)
    else:
      logging.info("送信先は現在オフラインです。")
      

    if chat_message_sent:
      self.response.out.write("正常に送信出来ました。");
    else:
      self.response.out.write("送信に失敗しました。");

def main():
  application = webapp.WSGIApplication(
      [('/xmpp/send', XmppSend)], debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()

