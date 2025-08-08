"""ASGI配置

它暴露了ASGI可调用对象作为模块级变量 ``application``。

更多信息请参见
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myhouse.settings')

application = get_asgi_application()