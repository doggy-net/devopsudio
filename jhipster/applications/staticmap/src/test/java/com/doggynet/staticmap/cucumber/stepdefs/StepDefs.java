package com.doggynet.staticmap.cucumber.stepdefs;

import com.doggynet.staticmap.StaticmapApp;

import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.web.WebAppConfiguration;
import org.springframework.test.web.servlet.ResultActions;

import org.springframework.boot.test.context.SpringBootTest;

@WebAppConfiguration
@SpringBootTest
@ContextConfiguration(classes = StaticmapApp.class)
public abstract class StepDefs {

    protected ResultActions actions;

}
