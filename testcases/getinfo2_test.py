# NOTE: Generated By HttpRunner v3.1.4
# FROM: testcases\getinfo2.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseGetinfo2(HttpRunner):

    config = (
        Config("testcase description")
        .variables(**{"n": 123})
        .base_url("${ENV(base_url)}")
        .verify(False)
    )

    teststeps = [
        Step(
            RunRequest("/login")
            .post("/login")
            .with_headers(
                **{
                    "Accept": "*/*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Connection": "keep-alive",
                    "Content-Length": "291",
                    "Host": "172.16.1.202:5000",
                    "Postman-Token": "88492415-74ee-4fc5-bd1a-68ec50415d8f",
                    "User-Agent": "PostmanRuntime/7.26.8",
                }
            )
            .with_data(
                {"username": "${get_username($n)}", "password": "${get_password()}"}
            )
            .extract()
            .with_jmespath("body.token", "token")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.message", "success")
        ),
    ]


if __name__ == "__main__":
    TestCaseGetinfo2().test_start()