def extract_instance_ids(log_data, instance_id_prefix):
    instance_ids = []
    for line in log_data:
        if instance_id_prefix in line:
            instance_id = line[line.index(instance_id_prefix) + len(instance_id_prefix):].strip()
            if instance_id not in instance_ids:
                instance_ids.append(instance_id)
    return instance_ids


def write_grouped_log(source_file, instance_ids, log_data):
    prefix = source_file[:10]
    output_file_name = f"{prefix} grouped.log"
    with open(output_file_name, 'w') as output_file:
        for instance_id in instance_ids:
            output_file.write(f"Instance ID: {instance_id}\n")
            for line in log_data:
                if "Instance Id =" in line and instance_id in line:
                    output_file.write(f"Entity ID: {line[line.index('"entityId":') + 11:line.index('"entityId":') + 49].strip()}\n")
                    start_index = line.index('"entityName":') + len('"entityName":') + 1
                    end_index = line.index('"', start_index)
                    entityName = line[start_index:end_index]
                    output_file.write(f"Entity Name: {entityName}\n")
                if instance_id in line:
                    output_file.write(line)
            output_file.write("\n")


def process_log_file(source_file):
    try:
        with open(source_file, 'r') as file:
            log_data = file.readlines()
        instance_id_prefix = "Instance Id = "
        instance_ids = extract_instance_ids(log_data, instance_id_prefix)
        write_grouped_log(source_file, instance_ids, log_data)
    except FileNotFoundError:
        print(f"Error: The file {source_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
