import boto3
import json
import os.path
import sys


def cli():
    image_ids = sys.argv[1:]

    ec2_client = boto3.client('ec2')
    #boto3.set_stream_logger('')

    if os.path.exists(image_ids[0]):
        with open(image_ids[0], 'r') as f:
            manifest = json.load(f)

        image_ids = []
        for build in manifest['builds']:
            image_ids.append(build['artifact_id'].split(':')[1])


    print('[aws-ami-delete] searching ami(s): {image_ids}'.format(image_ids=str.join(', ', image_ids)))

    # get ami info
    images = ec2_client.describe_images(
        ImageIds=image_ids,
        Owners=['self']
    )

    if not len(images['Images']):
        print('[aws-ami-delete] ami(s) not found: {image_ids}'.format(image_ids=str.join(', ', image_ids)))
        exit(1)

    for image in images['Images']:
        image_id = image['ImageId']
        snapshot_id = image['BlockDeviceMappings'][0]['Ebs']['SnapshotId']

        # delete/deregister ami
        print('[aws-ami-delete] - deleting ami: {image_id}'.format(image_id=image_id))
        ec2_client.deregister_image(
            ImageId=image_id
        )

        # delete associated snapshot
        print('[aws-ami-delete] - deleting snapshot: {snapshot_id}'.format(snapshot_id=snapshot_id))
        ec2_client.delete_snapshot(
            SnapshotId=snapshot_id
        )


if __name__ == '__main__':
    cli()
