package com.doggynet.topology.cucumber.stepdefs;

import com.doggynet.topology.TopologyApp;

import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.web.WebAppConfiguration;
import org.springframework.test.web.servlet.ResultActions;

import org.springframework.boot.test.context.SpringBootTest;

@WebAppConfiguration
@SpringBootTest
@ContextConfiguration(classes = TopologyApp.class)
public abstract class StepDefs {

    protected ResultActions actions;

}
