#ifndef __CONFIG_PARAMETERS_HPP__
#define __CONFIG_PARAMETERS_HPP__

#include <cstdint>

struct t6137 {
    constexpr static std::uint8_t chip = 8;
    constexpr static std::uint8_t channel = 6;
    constexpr static std::uint16_t block = 2048;
    constexpr static std::uint16_t pages = 128;
    constexpr static std::uint16_t pageSize = 4096;
    constexpr static std::uint16_t ti = 2048;
};

#endif