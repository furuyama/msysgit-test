�yGoogle App Engine �� XMPP�v���g�R�����g�p����Google Talk�Ƀ��b�Z�[�W�𑗐M����z

1. XMPP�v���g�R�����g�p���邽�߂̏���
"from google.appengine.api import xmpp" �Ɠ��͂��Axmpp�v���g�R�����C���|�[�g���܂��B

2. XMPP Python API�̎g�p
get_presence(jid, from_jid=None)
->Google Talk���[�U�̃I�����C���E�I�t���C���󋵂̎擾

send_message(jids, body, from_jid=None, message_type=MESSAGE_TYPE_CHAT, raw_xml=False)
->�����Ɏw�肵�����[�U�ɁA�����Ɏw�肵�����b�Z�[�W�𑗐M
->�Ԃ�l�́A�ȉ���3��
  * xmpp.NO_ERROR: ����ɑ��M����
  * xmpp.INVALID_JID: �w�肵�����[�U�������݂��Ȃ�
  * xmpp.OTHER_ERROR: ��L2�ȊO�̃G���[

3. �\�[�X�R�[�h�̎g�p���@
�ϐ� to_address�ɑ��M���Gmail�A�h���X����͂��Ă��������B
�������A���M�惆�[�U�����̃A�v���P�[�V�������`���b�g�ɏ��҂��Ă���K�v������܂��B
(�������Ȃ��ƃX�p���I�Ƀ��b�Z�[�W������܂����Ă��܂�����)

4. ���̃A�v���P�[�V������Google App Engine�Ƀf�v���C���Ă������B
�����[�J���Ŏ����Ă��鎞�̓R���\�[���Ƀ��O���o�邾���ŁAGTalk�ɂ͑���܂���


[�Q�l]
The XMPP Python API(XMPP�̊T�v�⃊�t�@�����X������܂�)
http://code.google.com/intl/ja/appengine/docs/python/xmpp/


