#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

if __name__ == "__main__":
   ndk = os.environ["ANDROID_NDK_HOME"]
   os.system(ndk + "/ndk-build")
