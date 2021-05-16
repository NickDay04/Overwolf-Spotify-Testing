function myFunction() {
	var oReq = new XMLHttpRequest();
	oReq.open("PUT", "https://api.spotify.com/v1/me/player/pause");
	oReq.setRequestHeader("Authorization", "Bearer BQAGq2u9sdgC6YkfL0yx5kIzo0qTIIQ_rBS7ZEQiwJc3-4W0PO3QoMO25KAwW9hlK3e3N8CL9ZGZAH4saHHC6vc7wJ3wLtT0YXZzBgMb8Ab5S5cyTnD7keDn3FWqnRtELUpZZbdB9ZjYPnv0kLeTKv5lyfkdWArhvMmCWd-VAhr7jaAUL2MQ5aZMwmMYXOlLNqpCimc4_wbyi_nglOU4nE58e3sdhdSlfyWLKgEVGJAXnC1agn0_VZ17e6RHsovXRoGXWxqkvhtJgXdBH8T_lkclD2aw");
	// oReq.setRequestHeader("device_id", "dd9d11375d60526824305b61f5599e6257783f74");
	oReq.send();
}
