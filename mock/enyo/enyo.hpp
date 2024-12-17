#ifndef __ENYO_MOCK_HPP__
#define __ENYO_MOCK_HPP__

#include <cstdint>
#include <list>
#include <tuple>

namespace elib::enyo {

struct Ignore {

};
struct Reserve {
    std::uint16_t reserve;
};
struct Limit {
    std::uint16_t limit;
};


using AddressType = std::uint16_t;
using FileName = std::uint32_t;


class VirtualMemoryInterface {
public:
    virtual void writeData(std::uintptr_t offset,
                   void *data,
                   std::size_t size) noexcept = 0;

    virtual void readData(std::uintptr_t offset,
                  void *data,
                  std::size_t size) noexcept = 0;
};


class EnyoDriverApi {
protected:
    virtual void lock() noexcept = 0;
    virtual void unlock() noexcept = 0;
public:
    virtual bool init() noexcept = 0;
    virtual void pushWrAddress(AddressType address) noexcept = 0;
    virtual void pushRdAddress(AddressType address) noexcept = 0;
    virtual void copyPackage(std::uintptr_t destination, std::uint16_t size) noexcept = 0;
    [[nodiscard]] virtual bool isReadFull() const noexcept = 0;
    [[nodiscard]] virtual bool isWriteFull() const noexcept = 0;
    [[nodiscard]] virtual bool isReadEmpty() const noexcept = 0;
    [[nodiscard]] virtual bool isWriteEmpty() const noexcept = 0;
    [[nodiscard]] virtual bool isFSetReady() const noexcept = 0;
    [[nodiscard]] virtual std::uint8_t getHex(std::uint8_t offset) noexcept = 0;
    [[nodiscard]] virtual std::uint32_t getWrPackageCounter() noexcept = 0;
    [[nodiscard]] virtual std::uint32_t getRdPackageCounter() noexcept = 0;
};


class Error {

};


class LongName {
private:
    std::list<FileName> mpath{};
public:
    auto &path() noexcept {
        return mpath;
    }
};


class UserRequest {
public:
    UserRequest(LongName &name) {

    }

    [[nodiscard]] bool isCreated() const noexcept {
        return true;
    }
};


template <typename InitType>
class Enyo {
private:
    Error lastError;

public:
    using UserRequestType = UserRequest;

public:
    Enyo(VirtualMemoryInterface &vm, EnyoDriverApi &driver) {}

    [[nodiscard]] bool init(std::uintptr_t address) noexcept {
        return true;
    }

    [[nodiscard]] bool upload() noexcept {
        return true;
    }

    const Error &status() const noexcept {
        return lastError;
    }

    void openToWrite(UserRequestType &request, Limit limit, Reserve reserve, 
                    std::uint64_t time, std::uint16_t attribute) noexcept {

    }

    void runIteration() noexcept {

    }
};

}

#endif