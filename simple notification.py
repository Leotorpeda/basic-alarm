simple notification

CLIENT_VERSION = "29.0.0+snapshot"
if __name__ == '__main__':
    if len(sys.argv) != 2:

from .quantity import parse_quantity

    def test_job_apis(self):
        client = api_client.ApiClient(configuration=self.config)
        api = batch_v1_api.BatchV1Api(client)

        create_job_resp = api.create_namespaced_job(
            body=job_manifest, namespace='default')
        self.assertEqual(name, create_job_resp.metadata.name)


    def test_watch_configmaps(self):
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)
