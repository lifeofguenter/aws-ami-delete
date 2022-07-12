import json
import os.path
import sys
from typing import List, Dict

import boto3


def delete_snapshots(ec2_client: boto3.client, block_device_mappings: List[Dict]) -> None:
    for block_device_mapping in block_device_mappings:
        snapshot_id = block_device_mapping['Ebs']['SnapshotId']
        print(f'[aws-ami-delete] - deleting snapshot: {snapshot_id}')
        ec2_client.delete_snapshot(
            SnapshotId=snapshot_id
        )


def cli() -> None:
    image_ids = sys.argv[1:]

    if not len(image_ids):
        print(f'[aws-ami-delete] empty args')
        exit(1)

    if os.path.exists(image_ids[0]):
        with open(image_ids[0], 'r') as f:
            manifest = json.load(f)

        image_ids = []
        for build in manifest['builds']:
            if build['packer_run_uuid'] == manifest['last_run_uuid']:
                image_ids.extend(build['artifact_id'].split(','))

    for image_id in image_ids:
        if ':' in image_id:
            aws_region = image_id.split(':')[0]
            image_id = image_id.split(':')[1]
        else:
            aws_region = None

        ec2_client = boto3.client('ec2', region_name=aws_region)

        # get ami info
        images = ec2_client.describe_images(
            ImageIds=[image_id],
            Owners=['self']
        )

        if not len(images['Images']):
            print(f'[aws-ami-delete] ami not found: {image_id}')
            exit(1)

        # delete/deregister ami
        print(f'[aws-ami-delete] - deleting ami: {image_id}')
        ec2_client.deregister_image(
            ImageId=image_id
        )

        # delete associated snapshot(s)
        delete_snapshots(ec2_client, images['Images'][0]['BlockDeviceMappings'])


if __name__ == '__main__':
    cli()
