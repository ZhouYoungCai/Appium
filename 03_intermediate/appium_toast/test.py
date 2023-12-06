#!/usr/bin/env python
# -*- coding: utf-8 -*-


from hamcrest import *

assert_that("this is a string",has_length(16))
print(assert_that(1,close_to(0.5,0.5)))

# assert_that('abc',contains_string('d'))
assert_that(10,greater_than(9))
# assert_that(10,greater_than_or_equal_to(11))

assert_that("this is teststring",ends_with("ing"))
# assert_that("This is Aaa;a",equal_to("ThiS is Aaa;A"))

# assert_that(["this", "is"," aaaaa,bbbb"],contains_inanyorder(["is"]))
# assert_that("matchers", contains_inanyorder(*"hamcrest"))
assert_that("matcherstam", contains_inanyorder('h','a','m','c','r','e','s','t'))
assert_that(("matcherst", contains_exactly('a')))