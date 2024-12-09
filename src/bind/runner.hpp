#ifndef __ORDIS_HPP__
#define __ORDIS_HPP__
// #include <enyo/enyo.hpp>
#include "../mock/config_parameters.hpp"
#include <iostream>

struct t6137 {
  constexpr static std::uint16_t chip = 8;
  constexpr static std::uint16_t channel = 6;
  constexpr static std::uint16_t block = 2048;
};

class VirtualMemoryMock {};

class EnyoDriverMock {};

template <typename InitType> class EnyoMock {
  VirtualMemoryMock &vm;
  EnyoDriverMock &driver;

public:
  EnyoMock(VirtualMemoryMock &vm, EnyoDriverMock &driver)
      : vm{vm}, driver{driver} {}

  void show() {
    std::cout << InitType::chip << ' ' << InitType::channel << ' '
              << InitType::block << std::endl;
  }
};

template <typename InitType> class Runner {
  VirtualMemoryMock vm;
  EnyoDriverMock driver;
  EnyoMock<InitType> enyo;

public:
  Runner() : enyo{vm, driver} { enyo.show(); }
};

#endif