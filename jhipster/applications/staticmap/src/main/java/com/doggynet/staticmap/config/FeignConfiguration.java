package com.doggynet.staticmap.config;

import org.springframework.cloud.netflix.feign.EnableFeignClients;
import org.springframework.context.annotation.Configuration;

@Configuration
@EnableFeignClients(basePackages = "com.doggynet.staticmap")
public class FeignConfiguration {

}
