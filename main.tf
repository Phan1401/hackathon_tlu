terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "us-west-2"
}

resource "aws_instance" "app_server" {
  ami           = "ami-08d70e59c07c61a3a"
  instance_type = "t3.micro"  # t2.micro -> t3.micro

  # tags = {
  #   Name = "ExampleAppServerInstance" 
  # }
}
resource "aws_eip" "app_eip" {
  instance = aws_instance.app_server.id

  tags = {
    Name = "AppServerEIP"
  }
}
