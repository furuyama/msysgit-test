1. Google Docs API���������@
�v���O���������s����O�ɁCcreateNewDoc.py, showAllTitle.py���ꂼ��̃\�[�X���̃��[���A�h���X�ƃp�X���[�h�����g�̋Z�|�h���C���i�܂��͒P��gmail�A�J�E���g�j�ɕύX����D
���[�J���Ȋ��ł���΂��ꂾ���Ńv���O�����͓��삷��D
http://localhost:8080�ȉ���/show��t�������ƌ��݂̃h�L�������g�ꗗ���\������C/create��t��������GoogleDocuments�ɂR��ނ̐V�K�t�@�C�����쐬�D

2. Datastore �̃A�b�v���[�h�^�_�E�����[�h���������@
�E�o�C�i���t�@�C���ŃA�b�v���[�h�^�_�E�����[�h����ꍇ
�@�[����Test�f�B���N�g�������܂ňړ����C�ȉ��̃R�}���h�����s����
[Download]
appcfg.py download_data --application=<�ΏۂƂ������A�v���P�[�V������> --kind=<kind> --url=http://<�A�v���P�[�V������>.appspot.com/_ah/remote_api --filename=<�ۑ��������t�@�C����>

<�ۑ��������t�@�C����>�Ƃ�Mac�Ȃ�Ⴆ��/Users/s.yamazaki/Documents/data.dump�ȂǁD--kind==<kind>�̓I�v�V�����ŁC�_�E�����[�h���������f�����w��ł���D

[Upload]
appcfg.py upload_data --application=<�A�v���P�[�V������> --kind=<kind> --filename=<�ۑ��������t�@�C����> <�����炭app.yaml������t�H���_���w��Dsrc/�Ȃ�>

�������C���̕��@�ŃA�b�v���[�h�^�_�E�����[�h�ł���̂̓o�C�i���t�@�C���݂̂Ȃ̂ŁC�����܂Ńo�b�N�A�b�v�ɂ����Ȃ�Ȃ��D

�E�e�L�X�g�t�@�C��(csv)�ŃA�b�v���[�h�^�_�E�����[�h������@
�@������Test�f�B���N�g�������ɂĈȉ��̃R�}���h�����s
[Download]
appcfg.py download_data --config_file=bulkloader.yaml --filename=<�ۑ��������t�@�C����.csv> --kind=Account --url=http://<�A�v���P�[�V������>.appspot.com/_ah/remote_api

[Upload]
appcfg.py upload_data --config_file=bulkloader.yaml --filename=<�A�b�v���[�h�������t�@�C����.csv> --kind=Account --url=http://<�A�v���P�[�V������>.appspot.com/_ah/remote_api

