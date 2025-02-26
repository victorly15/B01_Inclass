SOURCE_FILE = '2024-08-08.log'
INSTANCEID = "Instance Id = "

with open(SOURCE_FILE, 'r') as file:
    log_data = file.readlines()

instance_ids = []
for line in log_data:
    if INSTANCEID in line:
        instance_id = line[line.index(INSTANCEID) + 14:line.index(INSTANCEID) + 50].strip()
        if instance_id not in instance_ids:
            instance_ids.append(instance_id)


prefix = SOURCE_FILE[:10]
output_file_name = f"{prefix} grouped.log"

with open(output_file_name, 'w') as output_file:
    for instance_id in instance_ids:
        output_file.write(f"Instance ID: {instance_id}\n")

        for line in log_data:
            if INSTANCEID in line and instance_id in line:
                output_file.write(f"Entity ID: {line[line.index('"entityId":') + 11:line.index('"entityId":') + 49].strip()}\n")
                start_index = line.index('"entityName":') + len('"entityName":') + 1
                end_index = line.index('"', start_index)
                entityName = line[start_index:end_index]
                output_file.write(f"Entity Name: {entityName}\n")

            if instance_id in line:
                output_file.write(line)
        output_file.write("\n")
