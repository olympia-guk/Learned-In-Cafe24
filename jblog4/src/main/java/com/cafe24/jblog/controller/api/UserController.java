package com.cafe24.jblog.controller.api;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.cafe24.jblog.dto.JSONResult;
import com.cafe24.jblog.service.UserService;

@Controller("userAPIController")
@RequestMapping("/user/api")
public class UserController {
	
	@Autowired
	private UserService userService;
	
	@ResponseBody
	@RequestMapping("/checkID")
	public JSONResult checkID(@RequestParam(value="id", required=true, defaultValue="") String id) {
		Boolean exist = userService.existID(id);		
		JSONResult result = JSONResult.success(exist);
		return result;
	}
}
