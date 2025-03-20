# Use the official WSO2 Micro Integrator image
FROM wso2/micro-integrator:latest

# Set working directory
WORKDIR /home/wso2carbon

# Define the MI version (you can change if needed)
ENV WSO2_MI_VERSION=4.3.0

# Switch to root user so we can set ownership and copy files
USER root

# Ensure that the required user exists
RUN id -u wso2carbon &>/dev/null || useradd -m -d /home/wso2carbon -s /bin/bash wso2carbon

# Create the deployment directory (for APIs) and set permissions
RUN mkdir -p /home/wso2carbon/wso2mi-${WSO2_MI_VERSION}/repository/deployment/server/synapse-configs/default/api/ \
    && chown -R wso2carbon:wso2 /home/wso2carbon \
    && chmod -R 777 /home/wso2carbon

# Copy your XML deployment files (APIs) into the correct folder
COPY --chown=wso2carbon:wso2 integrator_config/synapse-configs/default/api/ \
    /home/wso2carbon/wso2mi-${WSO2_MI_VERSION}/repository/deployment/server/synapse-configs/default/api/

# (Optional) Debugging step: list the files to verify they were copied
RUN ls -l /home/wso2carbon/wso2mi-${WSO2_MI_VERSION}/repository/deployment/server/synapse-configs/default/api/

# Switch back to the proper user for running the MI process
USER wso2carbon

# Expose the necessary ports
EXPOSE 8290 8253

# Start the WSO2 Micro Integrator
CMD ["/home/wso2carbon/wso2mi-4.3.0/bin/micro-integrator.sh"]
