#ifndef __INTERFACES_HPP__
#define __INTERFACES_HPP__

// #include <enyo/enyo.hpp>
#include <fstream>
#include <iostream>

// namespace ee = elib::enyo;
// class VirtualMemoryMock : public ee::VirtualMemoryInterface
// {
//     using si = std::ios;
//     static const char *metafileName;
//     std::fstream metafile;

// public:
//     VirtualMemoryMock();

//     void writeData(std::uintptr_t offset,
//                    void *data,
//                    std::size_t size) noexcept override;

//     void readData(std::uintptr_t offset,
//                   void *data,
//                   std::size_t size) noexcept override;

//     [[nodiscard]] bool isInit() const noexcept;

// };

// class EnyoDriverMock : public ee::EnyoDriverApi
// {
// private:
//     std::uint64_t wrPackageCounter;
//     std::uint64_t rdPackageCounter;

// protected:
//     void lock() noexcept override;
//     void unlock() noexcept override;
// public:
//     EnyoDriverMock();
//     bool init() noexcept override;
//     void pushWrAddress(ee::AddressType address) noexcept override;
//     void pushRdAddress(ee::AddressType address) noexcept override;
//     void copyPackage(std::uintptr_t destination, std::uint16_t size) noexcept override;
//     [[nodiscard]] bool isReadFull() const noexcept override;
//     [[nodiscard]] bool isWriteFull() const noexcept override;
//     [[nodiscard]] bool isReadEmpty() const noexcept override;
//     [[nodiscard]] bool isWriteEmpty() const noexcept override;
//     [[nodiscard]] bool isFSetReady() const noexcept override;
//     [[nodiscard]] std::uint8_t getHex(std::uint8_t offset) noexcept override;
//     [[nodiscard]] std::uint32_t getWrPackageCounter() noexcept override;
//     [[nodiscard]] std::uint32_t getRdPackageCounter() noexcept override;
// };

#endif