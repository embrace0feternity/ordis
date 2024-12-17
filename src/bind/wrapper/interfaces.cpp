#include "interfaces.hpp"

const char * VirtualMemoryMock::metafileName = "mordisfile.txt";

VirtualMemoryMock::VirtualMemoryMock() : ee::VirtualMemoryInterface()
{
}

void VirtualMemoryMock::writeData(std::uintptr_t offset,
                                  void *data,
                                  std::size_t size) noexcept
{
    metafile.open(metafileName, si::out | si::binary | si::app);
    if (metafile.is_open()) {
        metafile.seekg(offset);
        auto cdata = reinterpret_cast<char *>(data);
        metafile.write(cdata, size);
        metafile.close();
    }
}

void VirtualMemoryMock::readData(std::uintptr_t offset,
                                 void *data,
                                 std::size_t size) noexcept
{
    metafile.open(metafileName, si::in | si::binary);
    if (metafile.is_open()) {
        metafile.seekg(offset);
        auto cdata = reinterpret_cast<char *>(data);
        metafile.read(cdata, size);
        metafile.close();
    }
}

[[nodiscard]] bool VirtualMemoryMock::isInit() const noexcept {
    std::fstream temp(metafileName, si::out | si::binary | si::app);
    return temp.tellp() != 0;
}

/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////

EnyoDriverMock::EnyoDriverMock() : ee::EnyoDriverApi{},
                                   wrPackageCounter(0),
                                   rdPackageCounter(0) {}

void EnyoDriverMock::lock() noexcept
{
}

void EnyoDriverMock::unlock() noexcept
{
}

bool EnyoDriverMock::init() noexcept
{
    return true;
}

void EnyoDriverMock::pushWrAddress(ee::AddressType address) noexcept
{

    std::ignore = address;
}

void EnyoDriverMock::pushRdAddress(ee::AddressType address) noexcept
{
    std::ignore = address;
}

void EnyoDriverMock::copyPackage(std::uintptr_t destination, std::uint16_t size) noexcept
{
}

[[nodiscard]] bool EnyoDriverMock::isReadFull() const noexcept
{
    return false;
}

[[nodiscard]] bool EnyoDriverMock::isWriteFull() const noexcept
{
    return false;
}

[[nodiscard]] bool EnyoDriverMock::isReadEmpty() const noexcept
{
    // unused
    return false;
}
[[nodiscard]] bool EnyoDriverMock::isWriteEmpty() const noexcept
{
    return false;
}
[[nodiscard]] bool EnyoDriverMock::isFSetReady() const noexcept
{
    return true;
}
[[nodiscard]] std::uint8_t EnyoDriverMock::getHex(std::uint8_t offset) noexcept
{
    return 0xff;
}
[[nodiscard]] std::uint32_t EnyoDriverMock::getWrPackageCounter() noexcept
{
    return wrPackageCounter;
}
[[nodiscard]] std::uint32_t EnyoDriverMock::getRdPackageCounter() noexcept {
    return rdPackageCounter;
}