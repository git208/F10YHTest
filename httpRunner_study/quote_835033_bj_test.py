# NOTE: Generated By HttpRunner v3.1.4
# FROM: quote_835033_bj.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseQuote835033Bj(HttpRunner):

    config = Config("testcase description")

    teststeps = [
        Step(
            RunRequest("/v3/quotentrd5")
            .get("http://114.80.155.134:22016/v3/quotentrd5")
            .with_headers(
                **{
                    "Param": "-1|-1",
                    "Symbol": "835033.bj",
                    "Token": "MitakeWeb",
                    "User-Agent": "python-requests/2.25.1",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."content-type"', "text/plain; charset=UTF-8")
            .assert_equal("body", "bodyboyd")
        ),
    ]


if __name__ == "__main__":
    TestCaseQuote835033Bj().test_start()