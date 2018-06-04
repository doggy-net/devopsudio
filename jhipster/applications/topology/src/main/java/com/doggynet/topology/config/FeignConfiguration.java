package com.doggynet.topology.config;

import org.springframework.cloud.netflix.feign.EnableFeignClients;
import org.springframework.context.annotation.Configuration;

@Configuration
@EnableFeignClients(basePackages = "com.doggynet.topology")
public class FeignConfiguration {

}
