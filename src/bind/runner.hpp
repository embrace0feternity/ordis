#ifndef __RUNNER_HPP__
#define __RUNNER_HPP__

#include "wrapper/config_parameters.hpp"
#include "wrapper/interfaces.hpp"
#include <iostream>
#include <cstdint>
#include <list>
#include <charconv>
#include <memory>

template <typename InitType>
class Runner
{
    VirtualMemoryMock vm;
    EnyoDriverMock driver;
    ee::Enyo<InitType> enyo;

    using EnyoType = ee::Enyo<InitType>;
    using UserRequestType = typename EnyoType::UserRequestType;
    std::list<UserRequestType> rlist;
    const ee::Error &enyoStatus;

private:
    ee::LongName parse(std::string_view name)
    {
        ee::LongName longName;
        if (name.size() > 1)
        {
            auto &path = longName.path();
            std::size_t head = 0;
            while (name.size() != 0)
            {
                head = name.find('/', head);
                std::string_view word = name.substr(0, head);
                ee::FileName n;
                auto res = std::from_chars(word.data(), word.data() + word.size(), n);
                // if (result.ec == std::errc::invalid_argument) {
                //     throw
                // }
                path.push_back(n);
                name.remove_prefix(head + 1);
                head = 0;
            }
        }
        return longName;
    }

    inline ee::LongName parseName(std::string &name)
    {
        name += "/";
        return parse(name);
    }

public:
    Runner() : enyo{vm, driver}, rlist{}, enyoStatus{enyo.status()}
    {
         init();
    }

    bool init()
    {
        bool rt;
        if (!vm.isInit())
        {
            constexpr std::uint32_t N = InitType::chip * InitType::channel * InitType::block / 8;
            std::array<std::uint8_t, N> badTable{};
            rt = enyo.init(reinterpret_cast<std::uintptr_t>(badTable.data()));
        }
        else
        {
            rt = enyo.upload();
        }
        return rt;
    }

    void create(std::string name,
                std::uint16_t rawReserve,
                std::uint16_t rawLimit,
                std::uint64_t time,
                std::uint16_t attribute)
    {
        ee::LongName rname = parseName(name);
        ee::Reserve reserve{rawReserve};
        ee::Limit limit{rawLimit};
        std::unique_ptr<UserRequestType> request{new UserRequestType(rname)};
        enyo.openToWrite(*request.get(), limit, reserve, time, attribute);
        while (!request->isCreated())
        {
            enyo.runIteration();
        }
        rlist.push_back(std::move(*request.get()));
    }

    void runIteration(int iterationCounter = 1)
    {
        for (int i = 0; i < iterationCounter; ++i)
        {
            enyo.runIteration();
        }
    }
};

#endif