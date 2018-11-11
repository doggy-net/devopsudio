package com.doggynet.livemap.config;

import org.springframework.cloud.netflix.feign.EnableFeignClients;
import org.springframework.context.annotation.Configuration;

@Configuration
@EnableFeignClients(basePackages = "com.doggynet.livemap")
public class FeignConfiguration {

}
