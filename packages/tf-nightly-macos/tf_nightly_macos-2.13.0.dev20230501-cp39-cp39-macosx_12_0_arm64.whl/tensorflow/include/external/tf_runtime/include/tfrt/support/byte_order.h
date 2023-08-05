/*
 * Copyright 2020 The TensorFlow Runtime Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// This file contains defines, macros, and constants related to byte order.

#ifndef TFRT_SUPPORT_BYTE_ORDER_H_
#define TFRT_SUPPORT_BYTE_ORDER_H_

// Byte order defines provided by gcc. MSVC doesn't define those so
// we define them here.
// We assume that all windows platform out there are little endian.
#if defined(_MSC_VER) && !defined(__clang__)
#define __ORDER_LITTLE_ENDIAN__ 0x4d2
#define __ORDER_BIG_ENDIAN__ 0x10e1
#define __BYTE_ORDER__ __ORDER_LITTLE_ENDIAN__
#endif

namespace tfrt {

constexpr bool kLittleEndian = __BYTE_ORDER__ == __ORDER_LITTLE_ENDIAN__;

// TODO(b/148087476): Handle endian-ness consistently.
#if __BYTE_ORDER__ == __ORDER_LITTLE_ENDIAN__
#define ASSERT_LITTLE_ENDIAN()
#else
#define ASSERT_LITTLE_ENDIAN() \
  static_assert(false, "big-endian not yet supported here");
#endif

}  // namespace tfrt

#endif  // TFRT_SUPPORT_BYTE_ORDER_H_
