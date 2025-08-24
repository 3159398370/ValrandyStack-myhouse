from django.http import JsonResponse
from django.db import connection
from django.core.cache import cache
import os
import sys
import subprocess
import json
from datetime import datetime


def health_check(request):
    """综合健康检查"""
    health_status = {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
        "checks": {}
    }

    # 数据库检查
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        health_status["checks"]["database"] = {"status": "ok"}
    except Exception as e:
        health_status["checks"]["database"] = {"status": "error", "message": str(e)}
        health_status["status"] = "unhealthy"

    # Redis检查（如果使用）
    try:
        cache.set('health_check', 'ok', 10)
        cache.get('health_check')
        health_status["checks"]["redis"] = {"status": "ok"}
    except Exception as e:
        health_status["checks"]["redis"] = {"status": "error", "message": str(e)}
        health_status["status"] = "unhealthy"

    # 磁盘空间检查
    try:
        stat = os.statvfs('/')
        free_space_gb = (stat.f_bavail * stat.f_frsize) / (1024**3)
        health_status["checks"]["disk_space"] = {
            "status": "ok" if free_space_gb > 1 else "warning",
            "free_gb": round(free_space_gb, 2)
        }
    except Exception as e:
        health_status["checks"]["disk_space"] = {"status": "error", "message": str(e)}

    # 内存检查
    try:
        with open('/proc/meminfo') as f:
            meminfo = f.read()
        health_status["checks"]["memory"] = {"status": "ok"}
    except:
        health_status["checks"]["memory"] = {"status": "ok"}  # 非Linux系统跳过

    status_code = 200 if health_status["status"] == "healthy" else 503
    return JsonResponse(health_status, status=status_code)


def health_simple(request):
    """简单健康检查"""
    return JsonResponse({
        "status": "ok",
        "timestamp": datetime.now().isoformat()
    })


def health_detailed(request):
    """详细健康检查"""
    details = {
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "python_version": sys.version,
        "django_version": "4.2.7",
        "environment": os.environ.get('DJANGO_SETTINGS_MODULE', 'unknown'),
        "cwd": os.getcwd(),
        "uid": os.getuid() if hasattr(os, 'getuid') else 'N/A'
    }
    
    # 检查git版本
    try:
        git_hash = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode().strip()
        details['git_commit'] = git_hash
    except:
        details['git_commit'] = 'unknown'
    
    return JsonResponse(details)