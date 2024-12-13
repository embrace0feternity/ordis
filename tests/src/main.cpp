#include "bind/mock/runner.hpp"
#include <fstream>
#include <gtest/gtest.h>

namespace ee = elib::enyo;

class OrdisTest : public testing::Test
{
protected:
    Runner<t6137> runner;
};


// Demonstrate some basic assertions.
TEST_F(OrdisTest, init)
{
    runner.create("123/467/7658/12", 1, 2, 3, 4);
    // Expect two strings not to be equal.
    EXPECT_STRNE("hello", "world");
    // Expect equality.
    EXPECT_EQ(7 * 6, 42);
}
