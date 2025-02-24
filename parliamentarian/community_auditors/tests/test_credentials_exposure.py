from parliamentarian import analyze_policy_string


class TestCredentialsManagement:
    """Test class for Credentials Management auditor"""

    def test_credentials_management(self):
        example_policy_string = """
        {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Action": [
                "redshift:getclustercredentials",
                "ecr:getauthorizationtoken"
              ],
              "Resource": "*"
            }
          ]
        }
        """
        policy = analyze_policy_string(
            example_policy_string, include_community_auditors=True
        )

        assert_equal(
            policy.finding_ids,
            set(
                [
                    "CREDENTIALS_EXPOSURE",
                    "PERMISSIONS_MANAGEMENT_ACTIONS",
                    "RESOURCE_STAR",
                ]
            ),
        )
