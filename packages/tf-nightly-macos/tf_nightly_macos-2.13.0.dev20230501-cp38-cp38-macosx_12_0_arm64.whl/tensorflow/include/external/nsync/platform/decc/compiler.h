/* Copyright 2016 Google Inc.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. */

#ifndef NSYNC_PLATFORM_DECC_COMPILER_H_
#define NSYNC_PLATFORM_DECC_COMPILER_H_

#define INLINE __inline
#define UNUSED
#define THREAD_LOCAL __declspec(thread)
#define HAVE_THREAD_LOCAL 1

#endif /*NSYNC_PLATFORM_DECC_COMPILER_H_*/
